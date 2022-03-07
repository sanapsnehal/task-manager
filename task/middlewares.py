from datetime import datetime
from django.shortcuts import render

from .models import RequestLog




class UnderConstructionsMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
         return render(request, 'task/underconstruction.html')





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
		user = 'snehal'
		rl = RequestLog(name=user, timestamp = datetime.now)
		rl.save()
		return response
	return my_function