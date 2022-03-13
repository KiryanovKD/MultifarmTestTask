from fastapi.testclient import TestClient

from app import BlockchainDataExtractionApp

from main import app

app.state.blockchain_app = BlockchainDataExtractionApp()
client = TestClient(app)


def test_read_revenue_from_task():
    response = client.get("/get_revenue_from_task")
    assert response.status_code == 200
    assert response.json() == {"income": {"ETH": "0.9551712893081763"}}