FROM python:3.10.3
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
