locust:
	@cd locust && \
		docker build -f Dockerfile -t locust .

stubby:
	@cd stubby && \
		docker build -f Dockerfile -t stubby .

build: locust stubby

start:
	@docker-compose up -d

stop:
	@docker-compose down -v

.PHONY: locust stubby
