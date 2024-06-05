# !bin/bash
gcloud config set project $PROJECT_ID

gcloud functions deploy server \
  --gen2 \
  --region=$LOCATION \
  --runtime=python310 \
  --source=./set2/image-caption-server \
  --entry-point=http_process_image\
  --min-instances=0\
  --trigger-http \
  --memory=1GB \
  --allow-unauthenticated \
  --run-service-account=$FUNCTIONS_SERVICE_ACCOUNT \
  --set-env-vars=PROJECT_ID=$PROJECT_ID,LOCATION=$LOCATION
