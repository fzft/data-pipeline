FROM bde2020/spark-master:2.4.5-hadoop2.7
MAINTAINER fzft

ENV SCALA_VERSION 2.11.8
ENV PYTHON_VERSION 3.6.5

#timezone
RUN apk add tzdata
RUN ls /usr/share/zoneinfo
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" >  /etc/timezone

# scala
RUN wget https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz && tar -zxvf scala-$SCALA_VERSION.tgz
RUN rm -rf scala-$SCALA_VERSION.tgz
ENV SCALA_HOME /scala-$SCALA_VERSION
ENV PATH "$PATH:$SCALA_HOME/bin"

#python 3.6
RUN apk add --update --no-cache build-base zlib-dev
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz && tar xvf Python-$PYTHON_VERSION.tgz
WORKDIR /Python-$PYTHON_VERSION
RUN ./configure --enable-optimizations --with-ensurepip=install && make -j 8
RUN make altinstall
RUN rm /usr/bin/python
RUN cd /usr/local/bin && ln -s python3.6 python


EXPOSE 8080 7077