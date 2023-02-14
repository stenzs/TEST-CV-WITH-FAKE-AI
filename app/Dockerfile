FROM python:3.11
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY ./ /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]