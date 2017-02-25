from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import client_data,admin_data
import requests
import random
import urllib
import urllib2
from django.core.mail import send_mail
from django.core.mail import EmailMessage



# Create your views here.
@csrf_exempt
def home_request(request):
	return render(request,"HomePage.html",{})	

@csrf_exempt	
def client_lrq(request):
	if request.method=='GET':
			return HttpResponseRedirect('/client_login') 

@csrf_exempt
def admin_erq(request):
	if request.method=='GET':
				return render(request,"admin_entries.html",{})	
	else:
		try:

			name=request.POST.get("name")
			number=request.POST.get("number")		
			emails=request.POST.get("email")
			project_id=request.POST.get("pro_id")
			project_deadline=request.POST.get("pro_deadline")

			randm=send_otp_mail_save(name,number,emails,project_id,project_deadline)
			if randm is not None:
				return render(request,"admin_entries.html",{})	
				#return http.HttpResponseRedirect('')
				#return render(request,"admin_login.html",{})		
		except Exception,e:
			print "Error saving details"


@csrf_exempt
def admin_lrq(request):
		if request.method=='POST':
			try:
				username=request.POST.get("username")
				password=request.POST.get("password")

				if username=="cnadmin" and password=="cnp":
					return HttpResponseRedirect('/admin_entries') 
				else:
				 	print "Invalid Details"					
			except Exception,e:
				print "Error Logging In"

		else:
				return render(request,"admin_login.html",{})	
			#return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
				#return render(request,"admin_login.html",{})	





@csrf_exempt
def send_otp_mail_save(name,number,emails,project_id,project_deadline):
	
	rand = random.randint(1000,9999)
	username=str(name)+str(rand)
	
	password=get_random_string(length=6, allowed_chars='ABCxyz1234567')
	
	email=EmailMessage('Code Nicely Username and Password to log in',"Username: "+str(username)+" and Password: "+str(password),to=[emails])
	email.send()
	

	client_data.objects.create(name=name,number=number,email=emails,project_id=str(project_id),project_deadline=str(project_deadline),username=str(username),password=str(password))
	

	authkey = "125195AvX4LUlVf57dcd941"
	mobiles = str(number)
	message = "Dear " +str(name)+", welcome to CODENICELY this is your Username and Password for logging in: "+str(username)+" and "+str(password)+"."
	sender = "CODNIC"
	route = "4"
	

	values = {
    	      'authkey' : authkey,
        	  'mobiles' : mobiles,
      	      'message' : message,
              'sender' : sender,
              'route' : route
              }
	

	url="http://api.msg91.com/api/sendhttp.php"

	postdata = urllib.urlencode(values)
	req = urllib2.Request(url, postdata)
	response = urllib2.urlopen(req)
	
	output = response.read() # Get Response
	
	return rand