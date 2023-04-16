FROM python:3.10

COPY . /src
COPY ./requirements.txt /src/requirements.txt
WORKDIR  /src
RUN chmod +x script.sh
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

EXPOSE 8000

CMD ./script.sh








