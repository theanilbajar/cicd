#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

# create image name
IMAGE_NAME = $TRAVIS_REPO_SLUG:$TAG

# build, tag and push to dockerhub
docker build -f Dockerfile -t $IMAGE_NAME .
docker tag $IMAGE_NAME $DOCKER_USER/$IMAGE_NAME
docker push $DOCKER_USER/$IMAGE_NAME