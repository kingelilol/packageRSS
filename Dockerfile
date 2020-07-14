FROM alpine

COPY supervisord.conf /etc/supervisor/
COPY httpd.conf /etc/

RUN apk add --no-cache python3 py3-pip firefox py3-lxml busybox-extras supervisor && \
    pip install selenium tinydb feedgen && \
    mkdir /install && \
    cd /install && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.24.0-linux64.tar.gz && \
    chmod +x geckodriver && \
    mv geckodriver /usr/bin/ && \
    mkdir /packageRSS && \
    echo "*/15 * * * * /usr/bin/python3 /packageRSS/src/packageRSS.py" | crontab - 


ENTRYPOINT ["supervisord", "-c" , "/etc/supervisor/supervisord.conf"]
