#!/bin/bash 

INIT_SHELL_DIR=`dirname $0`

sudo apt update
sudo apt install -y python3-pip

source ~/.bashrc

pip3 install --user pipenv && \
cd $INIT_SHELL_DIR/.. && \
#pipenv --python 3.5 && \
pipenv install

