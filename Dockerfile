FROM openjdk:8-jdk-slim

RUN apt-get update && apt-get install -y \
    python3 python3-pip wget procps curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY spark-3.5.3-bin-hadoop3.tgz /opt/spark.tgz
RUN tar -xvzf /opt/spark.tgz -C /opt && \
    mv /opt/spark-3.5.3-bin-hadoop3 /opt/spark && \
    rm /opt/spark.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY . /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]