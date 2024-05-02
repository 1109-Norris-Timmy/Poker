FROM python:3

RUN pip install awscli
RUN --mount=type=secret,id=aws,target=/root/.aws/credentials \
  aws s3 cp s3://... ...
  
WORKDIR /app

COPY Poker.py .
RUN chmod +x Poker.py 

ENTRYPOINT [ "/app/Poker.py" ]

