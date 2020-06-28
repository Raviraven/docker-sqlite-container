FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install cron

RUN mkdir /database

ADD crontab.txt /crontab.txt
ADD script.sh /script.sh
COPY entry.sh /entry.sh
RUN chmod 755 /script.sh /entry.sh
RUN crontab /crontab.txt
ENTRYPOINT [ "cron", "-f" ]