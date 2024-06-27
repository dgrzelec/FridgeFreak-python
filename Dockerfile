FROM python:3.11.9-alpine

LABEL org.opencontainers.image.source=https://github.com/dgrzelec/FridgeFreak-python

WORKDIR /usr/src/

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.11.0/wait wait
RUN chmod +x wait

COPY ./requirements.txt fridgefreak_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r fridgefreak_api/requirements.txt

COPY fridgefreak_api/*.py fridgefreak_api/
COPY fridgefreak_api/tests fridgefreak_api/tests

COPY fridgefreak_api/run.sh fridgefreak_api/run.sh
RUN chmod +x fridgefreak_api/run.sh

CMD ./wait && ./fridgefreak_api/run.sh