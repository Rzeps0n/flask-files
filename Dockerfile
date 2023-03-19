FROM alpine:latest
ARG TARGETARCH
WORKDIR /app
COPY . .
RUN apk add --no-cache python3 py3-pip
RUN pip install --upgrade flask
RUN touch hire_me
ENV PORT=5000
EXPOSE 5000
CMD [ "python3", "main.py" ]
