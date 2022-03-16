from datetime import datetime
from urllib import response
from django import views
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from .models import RequestLog
from datetime import datetime

obj_now = datetime.now()
time = obj_now.strftime("%H:%M")
time = str(time)
class UnderConstructionMiddleware:
	def __init__(self,get_response):
		self.get_response=get_response

	def __call__(self,request):
		if (time >= "10:46" and time < "17:00"):
			return render(request, 'underconstruction.html')
		else:
			return render(request,'home.html')
		# print("call From Middleware Before views")
		# response= render(request, 'underconstruction.html')
		# # response = HttpResponse("this site is underconstruction")
		# print("call from middleware after view")
		# return response



# class RequestLogMiddleware:
# 	def __init__(self,get_response):
# 		self.get_response = get_response

# 	def __call__(self, request):

# 		# user = self.get_response(request.user)
# 		user = 'snehal'
# 		rl = RequestLog(username=user, timestamp = datetime.now)
# 		rl.save()

def RequestLogMiddleware(get_response):
	def my_function(request):
		response = get_response(request)
		# user = 'snehal'
		if not request.user:
			return HttpResponseRedirect('login.html')
		rl = RequestLog(name=request.user, timestamp = datetime.now)
		rl.save()
		return response
	return my_function