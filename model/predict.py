from ultralytics import YOLO
from aws_lambda_powertools import Logger
from PIL import Image

logger = Logger()

def handler(event, context):
    img = event["path"]
    buf = Image.open(img)
    model = YOLO(f"../model/best.pt")

    results = model.predict(buf)
    result = results[0]

    response = {result.names[i]: result.probs.data.cpu().numpy()[i] for i in range(len(result.names))}
    logger.info(response)

    return {'statusCode': 200, 'body': response, 'headers': 'Content-Type: application/json'}

if __name__ == "__main__":
    event = {"path": "model/example/jack_1.jpg"}
    print(handler(event, None))