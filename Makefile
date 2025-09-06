.PHONY: install run clean

install:
	uv sync

run:
	uv run python app.py

clean:
	rm -rf .venv
	uv cache clean