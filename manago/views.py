from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import client_data,admin_data,temp_class
import requests
import random
import urllib
import urllib2
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse

dev_username=""
dev_password=""
client_username=""
client_password=""




# Create your views here.
@csrf_exempt
def home_request(request):
	return render(request,"HomePage.html",{})	

@csrf_exempt
def admin_login(request):
	if request.method=='GET':
		return render(request,"admin_login.html",{})

	if request.method=='POST':
		try:
			username=request.POST.get("username")
			password=request.POST.get("password")
			print str(username )
			print str(password)

			temp_class.objects.create(name=str(username))

			if str(username)=="cnadmin" and str(password)=="cnp":
				return render(request,"admin_entries.html",{})
			else:
		 		print "Invalid Details" 
		except Exception,e:
				print "Error Logging In"

		
@csrf_exempt
def client_entries(request):
	if request.method== 'GET':

		return render(request,"admin_entries.html",{})

	if request.method== 'POST':	
		try:
			print "client form"

			

			name=request.POST.get("name")	
			number=request.POST.get("number")		
			emails=request.POST.get("email")
			project_id=request.POST.get("pro_id")
			project_deadline=request.POST.get("pro_deadline")
			print "data fetched"
			randm=send_otp_mail_save_client(name,number,emails,project_id,project_deadline)
				
		except Exception,e:
			print "Error saving details"





@csrf_exempt
def send_otp_mail_save_client(name,number,emails,project_id,project_deadline):
	
	rand = random.randint(1000,9999)
	client_username=emails
	client_password=get_random_string(length=6, allowed_chars='ABCxyz1234567')
	
	'''email=EmailMessage('Code Nicely Username and Password to log in',"Username: "+str(username)+" and Password: "+str(password),to=[emails])
	email.send()'''
	

	
	'''
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
	'''
	
	return rand

@csrf_exempt
def send_otp_mail_save_developer(name,number,emails,team_id,role,project_id):
	
	rand = random.randint(1000,9999)
	username=emails
	
	password=get_random_string(length=6, allowed_chars='ABCxyz1234567')
	
	email=EmailMessage('Code Nicely Username and Password to log in',"Username: "+str(username)+" and Password: "+str(password),to=[emails])
	email.send()
	

	developer_data.objects.create(name=name,number=number,email=emails,team_id=str(team_id),role=str(role),project_id=str(project_id),username=str(username),password=str(password))
	

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