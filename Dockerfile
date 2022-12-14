FROM python:3.9

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /LunchPlace

# Install dependencies
COPY requirements.txt /LunchPlace/
RUN pip install -r requirements.txt

# Copy project
COPY . /LunchPlace/