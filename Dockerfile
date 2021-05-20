FROM python:3.8

ARG filepath
ENV filepath=$filepath

ADD textcorrect.py .

RUN pip install transformers sentencepiece python-docx flask

CMD ["python", "./textcorrect.py"]

EXPOSE 5000