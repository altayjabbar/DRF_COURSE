import json
from django.http import JsonResponse

def api_home(request,*args, **kwargs):
 
    body = request.body
    data = {}
    try:    
        data = json.loads(body)
    except:
        pass        
    print(data)

    # data['headers'] = request.headers 
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data["test"] = 12345
    return JsonResponse(data)
        