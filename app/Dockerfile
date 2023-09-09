# Build Python code to native binary manually, without third-party build containers
FROM python:alpine as build
COPY main.py .
RUN apk add libc-dev gcc upx && pip install pyinstaller && pyinstaller --onefile main.py && upx dist/main

FROM alpine:latest
COPY --from=build dist/main /app
# Fail-safe env
ENV AUTHOR="ra1nst0rm3d"
EXPOSE 8000
CMD ["./app"]
