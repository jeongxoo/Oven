from django.http import HttpResponse # Http로 응답 받음
from .sources.elastic import *

def searchElastic(request):
    es = connect()
    index = "ls_seoul_rank_info_idx"
    query = {
        "query" : {
            "match" : {
                "gu_name" : "노원구"
            }
        }
    }

    json = search(client = es, index = index, body = query)
    fp = json["hits"]["hits"][0]["_source"]["final_point"]
    rf = json["hits"]["hits"][0]["_source"]["rank_final"]
    return fp, rf