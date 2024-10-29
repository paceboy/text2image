#!/bin/bash

#用于切换公司和个人的代码库
#remote=ssh://liushaogeng@icode.baidu.com:8235/baidu/goodcoder/liushaogeng
remote=git@github.com:paceboy/text2image.git

#git clone --mirror $remote
git remote set-url origin $remote

