FROM ubuntu

RUN apt-get install ffmpeg libsm6 libxext6

FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . ./

CMD ["predict.handler"]