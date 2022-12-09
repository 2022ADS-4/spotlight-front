FROM python:3.10
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN mkdir -p app
COPY ./app app
EXPOSE 8501
EXPOSE 8000
ENTRYPOINT ["streamlit", "run"]
CMD ["app/app.py"]