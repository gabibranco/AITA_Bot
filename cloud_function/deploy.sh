gcloud builds submit --project studied-brace-202002 --tag gcr.io/studied-brace-202002/aita-bot .

gcloud run deploy aita-bot \
    --region=us-east4 --platform=managed --memory 512Mi \
    --allow-unauthenticated --image gcr.io/studied-brace-202002/aita-bot  \
    --set-env-vars "TWITTER_API_KEY=k9R0X67hA7gIzZDti5wHk48lK" \
    --set-env-vars "TWITTER_API_SECRET_KEY=jgwZaXVF8PepB0BuevIZhs7kP05Im4Fq7dDKMgOAxLARtmFbxM" \
    --set-env-vars "TWITTER_ACCESS_TOKEN=1335736860715462657-IPgsivMLzsPVaTwruXEezSIMBIr7Wl" \
    --set-env-vars "TWITTER_ACCESS_TOKEN_SECRET=02uT2WLJSpGlAYrklVolUkdoS1MBymQYPeqjtfzx826r3"