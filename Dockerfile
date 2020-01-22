FROM alpine:3.5
FROM python:3
RUN pip install --upgrade pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY buzz /src/buzz
COPY comic /src/comic
CMD python /src/app.py