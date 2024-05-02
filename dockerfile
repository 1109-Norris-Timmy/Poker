FROM python:3

RUN apk add --no-cache bash

WORKDIR /app

COPY Poker.py .
RUN chmod +x Poker.py 

ENTRYPOINT [ "/app/Poker.py" ]

