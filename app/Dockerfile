FROM moonbuggy2000/nuitka:py3.10-alpine-amd64 as build
WORKDIR /app
COPY main.py .
RUN python -m nuitka --standalone --onefile main.py
FROM alpine:latest as final
COPY --from=build /app/main.bin /app
CMD ["./app"]