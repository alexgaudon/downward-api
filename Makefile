.PHONY: install run clean build docker-run

install:
	pip install -r requirements.txt

run:
	python app.py

build:
	docker build -t downward-api .

docker-run:
	docker run -p 8080:8080 downward-api

clean:
	rm -rf .venv