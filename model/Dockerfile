FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./
RUN apt-get update && apt-get install libgl1
RUN pip3 install -r requirements.txt

COPY . ./

CMD ["predict.handler"]