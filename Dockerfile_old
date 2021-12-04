FROM python:3.9.7

WORKDIR /usr/app

COPY . .

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD [ "gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "--threads", "100", "app:app" ]
