# Sqlite3 docker container

Ubuntu based docker image with necessary tools for storing and backing up data.

## Components
- sqlite3 database
- cron
- python backup script
- python restore script

## How does it work?

Dockerfile creates an ubuntu based image, then:
- updates packages using update
- installs packages:
    - cron
    - python
- copies files
- starts cron

## How to run
1. Download or clone the repository
2. Edit crontab.txt - change time when cron executes script and/or command
3. Create .env file with
    - DATABASE_PATH
    - DB_BACKUP_DIR
    - DATABASE_NAME
4. Build docker image. 
    ```
    docker build --tag docker_image_name
    ```
5. Run docker image (remember to include .env file)
    ```
    docker run -it --rm -d --env-file .env docker_image_name
    ```

