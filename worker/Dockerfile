FROM python:3.7

RUN apt-get update
RUN apt-get install -y busybox-static wget git build-essential libboost-all-dev nkf
RUN apt-get clean

RUN wget http://lotus.kuee.kyoto-u.ac.jp/nl-resource/jumanpp/jumanpp-1.02.tar.xz
RUN tar Jxf jumanpp-1.02.tar.xz
RUN cd $project_dir/jumanpp-1.02 && ./configure && make && make install

# タイムゾーン設定
ARG project_dir=/work

# 必要なファイルをローカルからコンテナにコピー
RUN mkdir -p $project_dir

# requirements.txtに記載されたパッケージをインストール                         
WORKDIR $project_dir
ADD ./cron.edit /var/spool/cron/crontabs/root
ADD ./run.sh $project_dir
ADD ./download.sh $project_dir
RUN chmod 755 $project_dir/run.sh
RUN chmod 755 $project_dir/download.sh

ADD ./requirements.txt $project_dir

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# busybox crond -f -L /dev/stderr
CMD ["busybox", "crond", "-f", "-L", "/dev/stderr"]