# Build Python code to native binary manually, without third-party build containers
FROM python:slim as build
COPY main.py .
RUN apt-get update && apt-get install patchelf binutils --yes && pip install pyinstaller staticx \
    && pyinstaller --onefile main.py && staticx --strip dist/main dist/main-stat \
    && strip -s -R .comment -R .gnu.version --strip-unneeded dist/main-stat
RUN chmod -c 755 dist/main-stat && chown -c 0:0 dist/main-stat

FROM gcr.io/distroless/static-debian12
COPY --from=build dist/main-stat /app
# Fail-safe env
ENV AUTHOR="ra1nst0rm3d"
EXPOSE 8000
CMD ["./app"]
