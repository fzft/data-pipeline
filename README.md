# data-pipeline

## Requirements
* python 3.6

## Version


### build
* 根目录下 运行 make build
* 将 新生成的目录下的 . dist/jobs.zip, main.py 拷贝到 spark_work_node/spark_home/python/dist 目录下


### run
* spark-submit --py-files jobs.zip main.py --job <job_name> --master spark://spark.masternode.com:7077
* /spark/bin/spark-submit --py-files jobs.zip main.py --job example_job --master spark://spark-master:7077