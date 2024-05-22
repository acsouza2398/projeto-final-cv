FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./
RUN sudo apt-get install ffmpeg libsm6 libxext6
RUN pip3 install -r requirements.txt

COPY . ./

CMD ["predict.handler"]