import logging

import uvicorn
from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware

from app import BlockchainDataExtractionApp
from config import conf

app = FastAPI(openapi_url='/openapi.json', docs_url='/docs')


@app.exception_handler(Exception)
async def base_exc_handler(request: Request, exc: Exception):
    logging.error(f'Top Level Exception, error={exc}, exception={exc.__class__.__name__}')
    return Response(status_code=500)


@app.on_event("startup")
async def startup():
    blockchain_data_extraction_app = BlockchainDataExtractionApp()
    app.state.blockchain_app = blockchain_data_extraction_app


@app.get('/')
async def healthcheck():
    return Response(status_code=200)


@app.get('/get_transaction_receipt')
async def get_transaction_receipt(txhash: str):
    blockchain_app: BlockchainDataExtractionApp = app.state.blockchain_app
    resp = await blockchain_app.get_transaction_receipt(txhash)
    return resp


@app.get('/get_revenue_from_task')
async def get_revenue_from_task():
    blockchain_app: BlockchainDataExtractionApp = app.state.blockchain_app
    return await blockchain_app.get_revenue_from_task()


if __name__ == '__main__':
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                       allow_headers=["*"])
    uvicorn.run(app, host=conf.HOST, port=conf.PORT, access_log=True)
