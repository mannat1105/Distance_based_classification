FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install numpy pandas scikit-learn

CMD ["python", "test_script.py"]
