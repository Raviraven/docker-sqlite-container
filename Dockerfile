FROM nouchka/sqlite3:latest

RUN apt-get update
RUN apt-get install -y python
RUN mkdir /database
RUN mkdir /database-backup
COPY . /database/

WORKDIR /database
RUN touch db.sqlite3