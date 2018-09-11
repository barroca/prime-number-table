.PHONY: all build test destroy

IMAGE_NAME=prime-number-table-image


all: build

build: Dockerfile
	docker build -t ${IMAGE_NAME} .

test: build

destroy:
	docker images -a | grep ${IMAGE_NAME} | awk '{print $$3}' | xargs docker rmi

