FROM python:slim

WORKDIR /app
COPY . .

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y g++ && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt --no-cache-dir

CMD ["bot.py"]
ENTRYPOINT ["python3"]
