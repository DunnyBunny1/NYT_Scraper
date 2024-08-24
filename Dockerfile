# Use the Python 3.10 base image
FROM python:3.10
# Set the working directory to which all subsequent operations will be relative
WORKDIR /app
# Copy our dependencies - should already be pip compile
COPY ./requirements.txt ./
# Install our dependencies before copying source code so dependencies can be cached
# This will speed up future builds
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Put the command in an array of strings (exec form) rather than shell form
# This avoids creating a shell session
# Run our app's target function
CMD ["python", "app.main:prod"]
