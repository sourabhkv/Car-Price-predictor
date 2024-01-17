# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set work directory
WORKDIR /testproject

# Install dependencies
COPY requirement.txt /testproject/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirement.txt

# Copy project
COPY ./testproject /testproject/

# Run the server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]