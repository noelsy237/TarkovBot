FROM python:slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["bot.py"]
ENTRYPOINT ["python3"]