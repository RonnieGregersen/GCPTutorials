import os
from google.cloud import bigquery
from google.cloud import storage

# Set up your BigQuery configuration
project_id = "dit projekt ID"
dataset_id = "Dataset i bigquery"
table_id = "Tabel i bigquery"

def load_csv_to_bigquery(event, context):
    """Triggered by a change to a Cloud Storage bucket."""
    # Get the file details from the event
    bucket_name = event['bucket']
    file_name = event['name']
    
    # Skip processing if it's not a CSV file
    if not file_name.endswith('.csv'):
        return
    
    # Initialize the BigQuery client
    bq_client = bigquery.Client(project=project_id)
    
    # Prepare the BigQuery table reference
    table_ref = bq_client.dataset(dataset_id).table(table_id)
    
    # Prepare the Cloud Storage file path
    file_path = f"gs://{bucket_name}/{file_name}"
    
    # Load the CSV file into BigQuery
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )
    load_job = bq_client.load_table_from_uri(
        file_path, table_ref, job_config=job_config
    )
    
    # Wait for the load job to complete
    load_job.result()
    
    # Print the result
    print(f"File {file_name} loaded into BigQuery table {table_id}.")