From python:3.7-alpine

ADD requirements.txt /

RUN pip install -r /requirements.txt

Add setlight.py /

CMD ["python", "-u", "/setlight.py"]
