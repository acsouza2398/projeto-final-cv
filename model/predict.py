import os
import io
import json
import base64
import boto3
from ultralytics import YOLO
from dotenv import load_dotenv
from aws_lambda_powertools import Logger
from PIL import Image

logger = Logger()

def handler(event, context):
    logger.info(f"Image posting event: {event}")

    try:
        load_dotenv()
    
        body = json.loads(event['body'])
        image_data = base64.b64decode(body['image_data'])

        model = YOLO(f"best.pt")

        image = Image.open(io.BytesIO(image_data))
        results = model.predict(image)
        result = results[0]

        logger.info(f"Prediction result: {result}")

        response = {result.names[i]: float(result.probs.data.cpu().numpy()[i]) for i in range(len(result.names))}
        logger.info(response)

        return {
            'statusCode': 200,
            'body': json.dumps({"predictions": response}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

if __name__ == "__main__":
    event = {"path": "model/example/jack_1.jpg"}
    print(handler(event, None))
    