# 使用带有Python和Spark的基础镜像
FROM jupyter/pyspark-notebook

# 安装需要的Python库
RUN pip install jieba tensorflow ckiptagger gdown numpy pandas

# 拷贝你的Python脚本到工作目录
#COPY . /home/

# 设置工作目录
#WORKDIR /home/


