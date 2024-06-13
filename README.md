# finance-advisor-spanner



python -m streamlit run finance-advisor.py


gcloud config set project spanner-demos-ce
gcloud auth login

Authenticate with Google Cloud: gcloud auth login
Initialize your project: gcloud init
Build the container: gcloud builds submit --tag gcr.io/spanner-demos-ce/finance-advisor-app
Deploy the container: gcloud run deploy --image gcr.io/spanner-demos-ce/finance-advisor-app --platform managed --allow-unauthenticated
Access the app:
The deployment output wi