# Create your views here.
# coding=utf-8

from django.http import HttpResponse
from django.conf import settings
import json



def resolve_api(request):
	try:
		url = request.path
		file_name = settings.JSON_PATH + url.split("/")[-1]
	
		json_file= open(file_name)
		json_data = json.load(json_file)
		return HttpResponse(json.dumps(json_data), content_type="application/json")	
	except Exception, e:
		response_data = {
			'code':'-1',
			'msg':'unexpect api , you should check the url',
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")	
	