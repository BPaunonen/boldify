# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Copy all files from the current directory into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the HTML and CSS files to the container
COPY templates/index.html templates/index.html
COPY static/styles.css /static/styles.css

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Expose the port the Flask application is running on
EXPOSE 5000

# Run the command to start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]