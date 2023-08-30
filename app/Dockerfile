#FROM moonbuggy2000/nuitka:py3.10-alpine-amd64 as build
#WORKDIR /app
#COPY main.py .
#RUN python -m nuitka --standalone --onefile main.py
#FROM alpine:latest as final
#COPY --from=build /app/main.bin /app
# Fail-safe env
#ENV AUTHOR="ra1nst0rm3d"
#CMD ["./app"]

# Код ниже создаёт образ с тем же размером, но версии сборщика и Python - свежее

FROM python:alpine as build
COPY main.py .
RUN apk add libc-dev zstd gcc patchelf && pip install nuitka zstandard && python -m nuitka --onefile --lto=yes main.py
FROM alpine:latest as final
COPY --from=build main.bin /app
ENV AUTHOR="ra1nst0rm3d"
CMD ["./app"]