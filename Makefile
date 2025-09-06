.PHONY: install run clean build docker-run

install:
	pip install -r requirements.txt

build:
	docker build -t downward-api .

run: build
	docker run -p 8080:8080 downward-api

clean:
	rm -rf .venv
