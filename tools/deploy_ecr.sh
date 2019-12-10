#!/usr/bin/env bash
REGION="us-west-2"
REPO_NAME=${REPO_NAME:-""}
BASE="dkr.ecr.us-west-2.amazonaws.com"
if [[ -z $REPO_NAME ]]; then
    echo "REPO_NAME not found!"
    exit 1
fi
tag=$(aws ecr describe-images --repository-name $REPO_NAME --query 'reverse(sort_by(imageDetails,& imagePushedAt))[:1].imageTags' --output text --region $REGION --profile default 2>&1)
registry_id=$(aws ecr describe-images --repository-name $REPO_NAME --query 'reverse(sort_by(imageDetails,& imagePushedAt))[:1].registryId' --output text --region $REGION --profile default 2>&1)
URI=$registry_id.$BASE/$REPO_NAME:$tag
echo $URI
echo "Pull Image"
docker pull $URI
echo "Deploy Image"
docker run --name flaskApp -p 8080:80 $URI
