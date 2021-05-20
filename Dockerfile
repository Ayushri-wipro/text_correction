FROM python:3.8

WORKDIR /textcorrect.py 

COPY . .

RUN pip install transformers sentencepiece python-docx flask

CMD ["python", "./textcorrect.py"]

EXPOSE 5000