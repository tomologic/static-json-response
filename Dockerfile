FROM python:3-onbuild
COPY data.json /usr/src/app/data.json
EXPOSE 8080
CMD ["/usr/src/app/server.py"]
