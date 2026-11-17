from pymilvus import MilvusClient
from utils.milvus_utils import get_milvus_client
milvus_client = get_milvus_client()


print(milvus_client.list_collections())