FROM python:3.11.9

WORKDIR /usr/src/

COPY ./requirements.txt fridgefreak_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r fridgefreak_api/requirements.txt

COPY fridgefreak_api/*.py fridgefreak_api/
COPY fridgefreak_api/tests fridgefreak_api/

CMD ["fastapi", "run", "fridgefreak_api/main.py", "--port", "8000", "--reload"]