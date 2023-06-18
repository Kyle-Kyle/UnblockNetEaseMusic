FROM python:3.9.17-alpine3.17

RUN pip install requests bs4
ADD script.py /app/script.py

RUN touch /var/log/unblockneteasemusic.log
RUN echo "01 0 * * * python /app/script.py >> /var/log/unblockneteasemusic.log 2>&1" >> /var/spool/cron/crontabs/root
CMD crond && tail -f /var/log/unblockneteasemusic.log
