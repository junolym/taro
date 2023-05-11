FROM httpd

ARG USER_NAME=taro
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update \
 && apt-get install -y --no-install-recommends libapache2-mod-wsgi-py3 python3 python3-venv \
 && rm -rf /var/lib/apt/lists/*

ENV TZ Asia/Shanghai
ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH

ADD httpd.conf /usr/local/apache2/conf/httpd.conf
ADD taro /taro
RUN chmod +x /taro/cgi-bin/*
RUN mkdir /venv

RUN groupadd --gid $USER_GID $USER_NAME
RUN useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME
RUN chown $USER_NAME:$USER_NAME /usr/local/apache2 /taro /venv -R
WORKDIR /taro
USER $USER_NAME

RUN python3 -m venv /venv
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r /taro/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/taro/cgi-bin"
CMD ["httpd-foreground"]
