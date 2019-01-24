FROM python:3-slim

ADD requirements.txt .
RUN pip install -r requirements.txt
ADD gcloud_dns_updater.py .

CMD run_forever.sh
