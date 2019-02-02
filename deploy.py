from tasks import rebuild
import boto3
import os
from datetime import datetime
import subprocess

path = "output"
bucket_name = "ryancollingwood.info"
cloud_front_distribution_id = "E37U5FWWDNBQTH"

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

subprocess.call('pelican', shell=True)

invalidate_files = []

for root, subdirs, files in os.walk(path):

    for file_name in os.listdir(root):
        set_meta = False
        file_path = os.path.join(root, file_name)

        if os.path.isdir(file_path):
            continue
        else:     
            target_file = file_path.replace(path, "")[1:].replace("\\", "/")
            file_extension = os.path.splitext(file_path)[1]
            content_type = None

            if file_extension in ["", ".html", ".htm"]:
                invalidate_files.append(target_file)
                content_type = "text/html"           
            elif file_extension in [".css"]:
                invalidate_files.append(target_file)
                content_type = "text/css"

            print(target_file)

            # Do Stuff
            if content_type is not None:                
                with open(file_path, 'rb') as f:
                    data = f.read()                    
                    s3.Object(bucket_name, target_file).put(Body=data, ContentType=content_type)
            else:            
                s3_client.upload_file(file_path, bucket_name, target_file)


cloudfront = boto3.client('cloudfront')
cloudfront.create_invalidation(
    DistributionId=cloud_front_distribution_id,
    InvalidationBatch={
        'Paths': {
            'Quantity': len(invalidate_files),
            'Items': ['/{}'.format(f) for f in invalidate_files]
        },
        'CallerReference': 'my-references-{}'.format(datetime.now())
    }
)