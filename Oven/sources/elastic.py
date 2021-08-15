from elasticsearch import Elasticsearch, helpers

def connect():
    local = "localhost:9200"
    es = Elasticsearch(local)
    return es

def search(client, index, body):
    return client.search(index, body)

