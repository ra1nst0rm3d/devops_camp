# Build Python code to native binary manually, without third-party build containers
FROM python:alpine as build
COPY main.py .
RUN apk add libc-dev zstd gcc patchelf && pip install nuitka zstandard && python -m nuitka --onefile --lto=yes main.py

FROM alpine:latest
COPY --from=build main.bin /app
# Fail-safe env
ENV AUTHOR="ra1nst0rm3d"
EXPOSE 8000
CMD ["./app"]