from ultralytics import YOLO
import boto3
from dotenv import load_dotenv
import os
from aws_lambda_powertools import Logger

logger = Logger()

def handler(event, context):
    load_dotenv()

    if os.getenv("env") == "LOCAL":
        buf = event["path"]
        model = YOLO(f"model/best.pt")
    else:   
        s3 = boto3.client('s3',
                          region_name=os.getenv('AWS_REGION'),
                          aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                          aws_session_token=os.getenv('AWS_SESSION_TOKEN'))
        bucket = os.getenv("AWS_BUCKET_NAME")
        
        buf = s3.get_object(Bucket=bucket, Key=event["path"])["Body"].read()
        model = YOLO(f"/tmp/weights/best.pt")

    results = model.predict(buf)
    result = results[0]

    response = {result.names[i]: result.probs.data.cpu().numpy()[i] for i in range(len(result.names))}
    logger.info(response)

    return {'statusCode': 200, 'body': response, 'headers': 'Content-Type: application/json'}

if __name__ == "__main__":
    event = {"path": "model/example/jack_1.jpg"}
    print(handler(event, None))