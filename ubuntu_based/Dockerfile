FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install cron

RUN mkdir /database
RUN mkdir /scripts

ADD crontab.txt /scripts/crontab.txt
ADD script.sh /scripts/script.sh
COPY entry.sh /scripts/entry.sh

# copying python backup scripts
COPY /python_scripts/backup.py /scripts/backup.py
COPY /python_scripts/restore.py /scripts/restore.py

RUN chmod 755 /scripts/script.sh /scripts/entry.sh
RUN crontab /scripts/crontab.txt
ENTRYPOINT [ "cron", "-f" ]