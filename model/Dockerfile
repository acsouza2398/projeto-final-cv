FROM ubuntu

RUN apt-get update && apt-get -y install ffmpeg libsm6 libxext6 libgl1-mesa-dev libglib2.0-0

FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . ./

CMD ["predict.handler"]