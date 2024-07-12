# finance-advisor-spanner

## For changing instance and databases 
go to ```database.py``` and change these values
#### Cloud Spanner instance ID.
```instance_id = "spanner-fts"```
#### Cloud Spanner database ID.
```database_id = "mf-data"```

## For running locally
    

### Initialize your project 
    gcloud config set project spanner-demos-ce

    gcloud auth application-default login

    gcloud config set run/region us-central1

    pip3 install -r requirements.txt 

#### If using Service Account and Impersonation
    gcloud config set auth/impersonate_service_account finvest-app@spanner-demos-ce.iam.gserviceaccount.com
    gcloud auth application-default login --impersonate-service-account finvest-app@spanner-demos-ce.iam.gserviceaccount.com

    python3 -m streamlit run Home.py

## For Cloud Run Deployment:

### Build the container: 
    gcloud builds submit --tag gcr.io/span-cloud-testing/finance-advisor-app
### Deploy the container: 
    gcloud run deploy finance-advisor-app --image gcr.io/span-cloud-testing/finance-advisor-app --platform managed    --region us-central1

gcloud beta run services proxy finance-advisor-app --port=8080   


### Deploy to Google App Engine - Flex
gcloud app deploy 