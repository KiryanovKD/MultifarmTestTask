# MultifarmTestTask

To run:

1. Build docker image:
docker build -t multifarm .

2. Run docker container:
docker run -it --rm -p 8080:8080  -e "ETHERSCAN_API_KEY=YourApiKeyToken" multifarm 

You can find openapi docs here: http://0.0.0.0:8080/docs

You can get revenue from screenshot in task by this endpoint: http://0.0.0.0:8080/get_revenue_from_task

You can get all info about transaction by this endpoint: http://0.0.0.0:8080/get_transaction_receipt?txhash=TRANSACTION_HASH

Unfortunately, etnerscan provides access to historical price data only in the pro version of the API, so the response does not contain the price in USD
I didn't use Etnerscan python api libraries because they are synchronous
