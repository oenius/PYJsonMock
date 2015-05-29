# Create your views here.
# coding=utf-8

from django.http import HttpResponse
from django.conf import settings
import json



def resolve_api(request):
	url = request.path
	short_name = url.split("/")[-1]
	file_name = settings.JSON_PATH + url.split("/")[-1]
	try:
		try:
			json_file= open(file_name)
		except Exception, e:
			response_data = {
			'code':'-1',
			'msg':'JSON FILE ERROR: ' + short_name + ' file can not open, make sure it is exit',
			}	
			return HttpResponse(json.dumps(response_data), content_type="application/json")	
		try:
			json_data = json.load(json_file)
		except Exception, e:
			response_data = {
			'code':'-1',
			'msg':'JSON FORMATE ERROR: ' + short_name + ' file is exit,but you should check your json file',
			}	
			return HttpResponse(json.dumps(response_data), content_type="application/json")	
		
		return HttpResponse(json.dumps(json_data), content_type="application/json")	
	except Exception, e:
		response_data = {
			'code':'-1',
			'msg':'unexpect api , you should check the url',
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")	
	
