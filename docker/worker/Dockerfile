FROM bde2020/spark-worker:2.4.5-hadoop2.7

ENV SCALA_VERSION 2.11.8

#scala
RUN wget https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz && tar -zxvf scala-$SCALA_VERSION.tgz
ENV SCALA_HOME /scala-$SCALA_VERSION
ENV PATH "$PATH:$SCALA_HOME/bin"

#python 3.6
RUN apk add --update --no-cache build-base zlib-dev
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz && tar -zxvf Python-$PYTHON_VERSION.tgz
RUN cd Python-$PYTHON_VERSION && ./configure --enable-optimizations --with-ensurepip=install && make -j 8
RUN make install
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3.6  /usr/bin/python


EXPOSE 8081