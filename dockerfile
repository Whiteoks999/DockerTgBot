FROM python:3.11

RUN groupadd -r any \
&& useradd -g any -r -m any

USER any

WORKDIR /app

COPY --chown=any:any ./requirements.txt .

COPY --chown=any:any . .

RUN pip install -r requirements.txt


