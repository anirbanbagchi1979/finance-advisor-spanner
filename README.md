# finance-advisor-spanner


For running locally

Authenticate with Google Cloud: 
Initialize your project: 
    gcloud config set project spanner-demos-ce
    gcloud auth login
    gcloud config set run/region us-central1
    python -m streamlit run finance-advisor.py

For Cloud Run Deployment:


Build the container: 
    gcloud builds submit --tag gcr.io/spanner-demos-ce/finance-advisor-app
Deploy the container: 
    gcloud run deploy --image gcr.io/spanner-demos-ce/finance-advisor-app --platform managed --allow-unauthenticated
Access the app:
