.PHONY: typing
typing:
	docker compose run --rm typing

.PHONY: typing-pyright
typing-pyright:
	docker compose run --rm typing pyright .