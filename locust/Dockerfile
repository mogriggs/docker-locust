FROM python:3.6

RUN easy_install locustio pyzmq

EXPOSE 8089 5557 5558

ENTRYPOINT ["/usr/local/bin/locust"]

CMD ["-f", "locustfile.py", "--host=http://localhost"]
