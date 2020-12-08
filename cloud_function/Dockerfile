FROM python:3.8

WORKDIR /app

ADD ./Pipfile /app/Pipfile
ADD ./Pipfile.lock /app/Pipfile.lock
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy

ADD ./ /app

CMD ["python", "main.py"]