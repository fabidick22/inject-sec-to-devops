#!/usr/bin/env bash
container_id=$(docker ps -q 2>&1)
docker stop $container_id
docker rm $container_id