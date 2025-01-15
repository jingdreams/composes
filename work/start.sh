#!/bin/bash
dir="/mydata/pomelo-risk"
cd $dir
oldtag=$(cat tag)
date +%y%m%d%H%M%S > tag
tag=$(cat tag) docker-compose up -d --build
docker rmi pomelo-risk:${oldtag}