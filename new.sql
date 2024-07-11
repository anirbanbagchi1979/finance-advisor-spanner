gcloud dataflow jobs run gcloud-import --gcs-location=gs://staging-spanner-df/2.34/import/template --region=us-central1 --parameters='instanceId=anirban-test,databaseId=mf-data,inputDir=eu-mf-demo/export/spanner-fts-mf-data-2024-06-27_14_29_49-16088248389294857164,spannerHost=https://wrenchworks-loadtest.googleapis.com'


