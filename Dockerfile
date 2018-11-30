FROM python:3-alpine

ADD requirements.txt .
RUN pip install -r requirements.txt
ADD gcloud_dns_updater.py .

CMD python gcloud_dns_updater.py
