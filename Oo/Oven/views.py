from django.http import HttpResponse # Http로 응답 받음
from .sources.elastic import *

def searchElastic(request):
    es = connect()
    index = "d_search_test_1"
    query = {
        "query" : {
            "match" : {
                "core.title" : "코로나"
            }
        }
    }

    json = search(client = es, index = index, body = query)
    # fp = json["hits"]["hits"][0]["_source"]["final_point"]
    # rf = json["hits"]["hits"][0]["_source"]["rank_final"]
    print(json)
    return fp, rf