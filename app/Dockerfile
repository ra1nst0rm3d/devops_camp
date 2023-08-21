FROM python:slim
COPY app.yaml .
COPY main.py .
RUN pip install Flask
CMD ["python", "main.py"]