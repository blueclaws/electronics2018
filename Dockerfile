# Use an official Python runtime as a parent image
FROM python:3

RUN apt-get update && apt-get install -y mysql-server && rm -rf /var/lib/apt/cache

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
