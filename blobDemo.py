#! /usr/bin/python3


from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
acctname = '<Enter account name>'
token='<Enter SAS token>'
container='<Enter container name>'
filename='image1.jpg'
block_blob_service = BlockBlobService(account_name=acctname, sas_token=token, protocol='http')
block_blob_service.create_blob_from_path (container, filename, filename, content_settings=ContentSettings(content_type='image/jpg'))
generator = block_blob_service.list_blobs(container)
for blob in generator:
    print(blob.name)
