import os

import joblib
import numpy as np
from sanic import Sanic, response
from gensim.models.doc2vec import Doc2Vec
from twython import Twython

app = Sanic(__name__)


class Model:
    def __init__(self):
        self.xgb = joblib.load(
            os.path.dirname(os.path.realpath(__file__)) + "/xgb_model.joblib"
        )
        self.d2v = Doc2Vec.load(
            os.path.dirname(os.path.realpath(__file__)) + "/d2v.model"
        )

    def _vectorize(self, text):
        return np.array([self.d2v.infer_vector(text.split(" "))])

    def judge(self, text):
        return self.xgb.predict(self._vectorize(text))[0]


class Text(Model):
    def __init__(self):
        super().__init__()
        self.title_generator = joblib.load(
            os.path.dirname(os.path.realpath(__file__)) + "/markovify.joblib"
        )

    def generate(self):
        title = ""
        while not (
            (title.lower().count("wibta") == 1 and title.lower().count("aita") == 0)
            or (title.lower().count("aita") == 1 and title.lower().count("wibta") == 0)
        ):
            title = self.title_generator.make_short_sentence(140)
        return {"text": title, "judgment": self.judge(title)}


t = Text()

twitter = Twython(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET_KEY"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
)


@app.route("/post")
async def main(request):
    text_and_judgment = t.generate()
    text = text_and_judgment["text"]
    judgment = text_and_judgment["judgment"]
    post = twitter.update_status(status=text)
    post_id = post["id"]
    twitter.update_status(status=judgment, in_reply_to_status_id=post_id)
    return response.json(True)


@app.route("/")
async def status(request):
    return response.json(True)


app.run(host="0.0.0.0", port=os.getenv("PORT"))