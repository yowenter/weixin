FROM python:2.7.8
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/
RUN pip install -r  requirements.txt
COPY . /usr/src/app
EXPOSE 4000
CMD ["python","app/app.py"]
