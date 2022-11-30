FROM python:3.11

RUN pip3 install --upgrade faker

WORKDIR "/src"

COPY anonymization ./anonymization
COPY __init__.py ./
COPY main.py ./

CMD [ "python3", "main.py" ]