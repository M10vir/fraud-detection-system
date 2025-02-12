# deepseek_integration/cosmos_db.py

from azure.cosmos import CosmosClient

def save_insights_to_cosmos_db(insights, transaction_id):
    """
    Save insights to Azure Cosmos DB.
    """
    # Initialize Cosmos DB client
    cosmos_client = CosmosClient("your-cosmos-db-endpoint", "your-cosmos-db-key")
    database = cosmos_client.get_database_client("fraud-detection-db")
    container = database.get_container_client("insights")

    # Save insights
    insight_item = {
        "id": transaction_id,
        "transaction_id": transaction_id,
        "insights": insights,
        "timestamp": "2023-10-01T12:34:56"  # Replace with actual timestamp
    }

    container.upsert_item(insight_item)
    print("Insights saved to Azure Cosmos DB.")

if __name__ == "__main__":
    # Sample insights (replace with actual insights from DeepSeek-R1)
    insights = {
        "risk_score": 0.85,
        "recommendations": ["Flag for review", "Notify customer"]
    }

    # Save insights to Cosmos DB
    save_insights_to_cosmos_db(insights, "12345")