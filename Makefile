.PHONY: all build test destroy

IMAGE_NAME=prime-number-table-image
PRIMES=10
build: Dockerfile
	docker build -t ${IMAGE_NAME} .

run:
	docker run ${IMAGE_NAME} ${PRIMES}

test:
	docker run -t --rm ${IMAGE_NAME} py.test tests/

destroy:
	docker images -a | grep ${IMAGE_NAME} | awk '{print $$3}' | xargs docker rmi
