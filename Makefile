PROJECT_NAME=anonymize-pii-app

build:
	@docker build -t ${PROJECT_NAME}:latest .

run:
	@docker run -it -v "$$(pwd)"/output:/output ${PROJECT_NAME}:latest 

build-test:
	@docker build -f Dockerfile.test -t ${PROJECT_NAME}-test:latest .

test: build-test
	@docker run -it --rm ${PROJECT_NAME}-test:latest