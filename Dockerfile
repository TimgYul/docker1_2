FROM python:3.10

COPY . /src
WORKDIR  /src
RUN chmod +x script.sh
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ./script.sh








