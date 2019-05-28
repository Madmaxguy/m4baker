FROM python:2.7.16
#FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

# 1. Install PyQT4 dependencies

RUN apt-get update && apt-get install -y \
python-dev python-qt4 python-qt4-dev python-sip python-sip-dev build-essential gfortran libqt4-dev qt4-qmake libpq-dev libsqlite3-dev qt4-dev-tools qt4-doc unixodbc-dev pyqt4-dev-tools


# 2. Install packages
#RUN cat /etc/*-release # This is Debian 9 (stretch)
#echo "deb http://www.deb-multimedia.org stretch main" >> /etc/apt/sources.list &&

RUN echo "deb http://www.deb-multimedia.org stretch main" >> /etc/apt/sources.list && \
	apt-get update && \
 	apt-get install deb-multimedia-keyring -y --allow-unauthenticated && \
 	apt-get install -y libfaac-dev --allow-unauthenticated

RUN apt-get update && apt-get install -y \
	wget \
	git \
	curl \
	faac \
	ffmpeg \
	libasound2-plugins mp4v2-utils libmp4v2-2 \
	libfaac-dev \
	libasound2 libsox-fmt-all libsox-dev sox libstdc++6

# to be installed
# ffmpeg libasound2-plugins mp4v2-utils libmp4v2-2 faac

# 3. Download repo and install dependencies
RUN git clone https://github.com/Madmaxguy/m4baker.git && \
	cd m4baker/deps/ && \
	cd sip-4.19.17 && \ 
	python configure.py && make && make install && \
	pwd

# 4. Install PyQt
RUN	cd /m4baker/deps/PyQt4_gpl_x11-4.12.3 && \
	echo yes | python configure-ng.py && \
	echo "Executing make" && \
	make && \
	echo "Executing make install" && \
	sudo make install && \
	cd ../../ && \
	python -m pip install -r requirements.txt && \
	python setup.py install --optimize=1

# 4. Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/mshepelev && \
    echo "mshepelev:x:${uid}:${gid}:mshepelev,,,:/home/mshepelev:/bin/bash" >> /etc/passwd && \
    echo "mshepelev:x:${uid}:" >> /etc/group && \
    echo "mshepelev ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/mshepelev && \
    chmod 0440 /etc/sudoers.d/mshepelev && \
    chown ${uid}:${gid} -R /home/mshepelev


USER mshepelev
ENV HOME /home/mshepelev
CMD /usr/local/bin/m4baker
