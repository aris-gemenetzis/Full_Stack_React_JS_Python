# Use Python base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /front

# Copy requirements file (pip freeze > requirements.txt) into container
COPY ./requirements.txt /front/requirements.txt

# Install package dependencies
RUN pip install --no-cache-dir --upgrade -r /front/requirements.txt

# Copy FastAPI app into container
COPY ./app /front/app

# Set run command argumnets (strings)
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]