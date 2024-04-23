FROM python:3.9
WORKDIR /test
COPY . /test
RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader stopwords
CMD python python.py
