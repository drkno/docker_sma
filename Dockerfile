FROM python:2

WORKDIR /app

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install git python-setuptools ffmpeg && \
    rm -rf /var/lib/apt/lists/* && \
    pip install requests requests[security] requests-cache babelfish "guessit<2" "subliminal<2" qtfaststart deluge-client && \
    pip uninstall --yes stevedore && \
    pip install stevedore==1.19.1 python-dateutil && \
    mkdir /config && \
    mkdir /files && \
    git clone https://github.com/mdhiggins/sickbeard_mp4_automator.git base && \
    apt-get --yes autoremove git

COPY ./wrapper .

VOLUME /config
VOLUME /files

EXPOSE 7784

CMD ["python", "start.py"]
