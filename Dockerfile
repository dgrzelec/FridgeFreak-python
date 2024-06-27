FROM python:3.11.9-alpine

ARG PORT=8000
LABEL org.opencontainers.image.source=https://github.com/dgrzelec/FridgeFreak-python

WORKDIR /usr/src/

COPY ./requirements.txt fridgefreak_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r fridgefreak_api/requirements.txt

COPY fridgefreak_api/*.py fridgefreak_api/
COPY fridgefreak_api/tests fridgefreak_api/tests

ENV PORT=${PORT}
CMD ["sh", "-c", "fastapi run fridgefreak_api/main.py --port ${PORT}"]
