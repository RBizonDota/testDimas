FROM python:3.8
WORKDIR /code

COPY . /code

CMD ["python", "test_script.py"]