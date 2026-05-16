import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_name = "edvo-downloads-videos"
        object_key = "videos/solarsystem.mp4"   # example: demo.mp4

        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_key
            },
            ExpiresIn=60   # URL valid for 60 seconds
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "url": url
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
