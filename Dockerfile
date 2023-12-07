# Filename: Dockerfile

# Set base image (host OS)
FROM python:3.11.7-alpine3.18

# By default, listen on port 5000
EXPOSE 5000/tcp

# Copy the content of the local src directory to the working directory
COPY . /app

# Set the working directory in the container
WORKDIR /app

# Install any dependencies
RUN pip install -r requirements.txt

# Specify the command to run on container start
ENTRYPOINT ["python"]
CMD ["app.py"]