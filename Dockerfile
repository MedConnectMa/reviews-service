FROM python:3.11.3

# set working directory
WORKDIR /app

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# copy source code
COPY . .

# run server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
