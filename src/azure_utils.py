import os

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv("configiration.env")

azure_connection_string = os.environ.get("AZURE_STORAGE_STRING")
container = os.environ.get("CONTAINER_NAME")


def upload_data_azure(blob_address, data):
    """data upload in azure...
    - blob address: file path in a container with file name to be saved.
    """

    # Connect to Azure Storage
    blob_service_client = BlobServiceClient.from_connection_string(
        azure_connection_string
    )
    # Select the container and destination filename
    blob_client = blob_service_client.get_blob_client(
        container=container,
        blob=blob_address,  # filepath with filename to be saved
    )
    # uploading to storage
    blob_client.upload_blob(data, overwrite=True)
