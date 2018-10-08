# Use an official Python runtime as a parent image
FROM ubuntu:18.04
FROM python:3

RUN  apt-get update
RUN  apt-get install -y mysql-server

# Set the working directory to /app
WORKDIR /site

# Copy the current directory contents into the container at /app
COPY . /site

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run bash script when the container launches
CMD ["./start"]
