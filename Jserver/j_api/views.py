# Create your views here.
# coding=utf-8

from django.http import HttpResponse
from django.conf import settings
import json
import markdown


def resolve_api(request):
    request.encoding = "gb2312"
    url = request.path
    short_name = url.split("/")[-1]
    file_name = settings.JSON_PATH + url.split("/")[-1]

    try:
        try:
            json_file = open(file_name)
            if short_name == "index.html":
            	json_file =open(settings.JSON_PATH +"index.md")
            	md = markdown.Markdown()
            	html = md.convert(json_file.read().decode('utf-8'))
            	return HttpResponse(html,content_type="text/html; charset=utf-8")
        except Exception, e:
            response_data = {
                'code': '-1',
                'msg': 'JSON FILE ERROR: ' + short_name + ' file can not open, make sure it is exit',
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        try:
            json_data = json.load(json_file)
        except Exception, e:
            response_data = {
                'code': '-1',
                'msg': 'JSON FORMATE ERROR: ' + short_name + ' file is exit,but you should check your json file',
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        return HttpResponse(json.dumps(json_data), content_type="application/json")
    except Exception, e:
        response_data = {
            'code': '-1',
            'msg': 'unexpect api , you should check the url',
        }
        return HttpResponse(json.dumps(response_data), content_type="application/json")
