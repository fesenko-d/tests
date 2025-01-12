FROM alpine

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY App .

EXPOSE 8000

CMD ["python3", "-m", "http.server"]
