#!/bin/bash

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker pull auswar/team2_project:latest

              