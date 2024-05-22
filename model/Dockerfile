# Use the official AWS Lambda Python image as a base
FROM public.ecr.aws/lambda/python:3.10

# Install necessary packages
RUN yum -y update \
    && yum -y install \
       libGL \
       mesa-libGL \
       mesa-libGLU \
       libXext \
       libSM \
       libXrender \
       ffmpeg \
       libglib2.0-0

# Copy your function code
COPY . ${LAMBDA_TASK_ROOT}

# Copy requirements.txt and install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip3 install -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Set the CMD to your handler
CMD ["predict.handler"]
