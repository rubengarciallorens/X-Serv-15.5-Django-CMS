from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

# Create your views here.
def list (request, identification):
	try:
		page=Pages.objects.get(id=identification)
		response=page.page
	except:
		response="Page:  " + str(identification) + " is not saved \n"

	return HttpResponse(response)
