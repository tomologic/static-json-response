build:
	docker build --force-rm -t tomologic/$(shell basename $(CURDIR)) .
run:
	docker run -p "8080:8080" tomologic/$(shell basename $(CURDIR))
push:
	docker push tomologic/$(shell basename $(CURDIR))
