FROM python:3.10

RUN pip3 install dataclasses
RUN pip3 install aiohttp
RUN pip3 install pydantic
RUN pip3 install uvicorn[standard]
RUN pip3 install fastapi

WORKDIR /app
COPY . .

EXPOSE 8080
WORKDIR /app/src

CMD ["python3", "main.py"]