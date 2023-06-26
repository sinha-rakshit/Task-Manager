FROM python:3.9

RUN pip install mysql-connector-python

WORKDIR .

COPY . .


ENV DB_HOST=localhost
ENV DB_USER=root
ENV DB_PASSWORD=Qwerty@123
ENV DB_DATABASE=test

CMD ["python" , "main.py"]


