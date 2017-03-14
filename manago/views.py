from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Count
import requests
import random
import urllib
import urllib2
import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# Create your views here.
@csrf_exempt
def home_request(request):
	return render(request,"HomePage.html",{})	

@csrf_exempt
def admin_login(request):
	if request.method=='GET':
		return render(request,"admin_login.html",{})	

	else:
		try:
			username=request.POST.get("username")
			password=request.POST.get("password")
			print str(username)
			print str(password)
			try:
				qry=admin_data.objects.get(username=str(username),password=str(password))
				if qry is not None:
					return HttpResponseRedirect('/client_verify/')					
				
				else:
					return render(request,"admin_login.html",{})					
		 			print "Invalid Details" 
 			except Exception,e:
 				print str(e)
 				return render(request,"admin_login.html",{})					

		except Exception,e:
				print str(e)
				return render(request,"admin_login.html",{})					
				

		
@csrf_exempt
def client_entries(request):
	if request.method=='GET':
		return render(request,"admin_entries.html",{})

	else:
		try:
			name=request.POST.get("name")	
			number=request.POST.get("number")		
			emails=request.POST.get("email")
			project_id=request.POST.get("pro_id")

			project_deadline=request.POST.get("pro_deadline")

			try:
				query=client_data.objects.get(email=emails)
			except Exception,e:
				query=None				

			if query is not None:
				print "Client already exists"
				return render(request,"admin_entries.html",{})			
			else:
				client_password=send_otp_mail_save_client(name,number,emails,project_id,project_deadline)
				client_data.objects.create(name=name,number=number,email=emails,project_id=project_id,project_deadline=project_deadline,password=client_password)	
				print "working"
				return render(request,"admin_entries.html",{})

		except Exception,e:
			print str(e)
			print "Error saving details"
			return render(request,"admin_entries.html",{})			

@csrf_exempt			
def verify_flag_page(request):
	return render(request,"admin_entries.html",{})
	
@csrf_exempt
def developer_entries(request):
	if request.method=='GET':
		return render(request,"admin_entries.html",{})

	else:
		try:
			#print "developer form"
			name=request.POST.get("dname")	
			number=request.POST.get("dnumber")		
			emails=request.POST.get("demail")
			team_id=request.POST.get("dteam_id")
			role=request.POST.get("drole")
			project_id=request.POST.get("dpro_id")
			
			#print "data fetched"
			verify_flag=developer_data.objects.get(email=emails)
			if verify_flag is None:
				client_password=send_otp_mail_save_developer(name,number,emails,team_id,role,project_id)
				developer_data.objects.create(name=name,number=number,email=emails,project_id=project_id,project_deadline=project_deadline,password=client_password)	
			else:
				print "Developer already exists"
				return render(request,"admin_entries.html",{})			

		except Exception,e:
			print "Error saving details"
			return render(request,"admin_entries.html",{})			

@csrf_exempt
def client_login(request):
	print str(request)
	if request.method=='GET':
		return render(request,"client_login.html",{})		
	else:
		try:
			cusername=request.POST.get("username")
			cpassword=request.POST.get("password")
			print cusername
			print cpassword
			
			try:
				query=client_data.objects.get(email=str(cusername),password=str(cpassword))
				
				if query is None:
					return render(request,"client_login.html",{})			
				else:
					uname=getattr(query,'name')
					request.session['uname']=uname
					print uname
					print "data valid"
					return HttpResponseRedirect('/client_panel/')
					#return render(request,"client_panel.html",{'client_call':True,'name':uname})
					
			except Exception,e:
				print str(e)
				
				return render(request,"client_login.html",{})			
		except Exception,e:
			print "failed to post"
			return render(request,"client_login.html",{})	

@csrf_exempt
def client_panel(request):
	uname=request.session['uname']
	if request.method=='GET':
		return render(request,"client_panel.html",{'name':uname})		
	

@csrf_exempt
def all_docs(request):
	return render(request,"all_docs.html")		




@csrf_exempt
def developer_panel(request):
	uname=request.session['uname']
	mailid=request.session['mailid']

	if request.method=='GET':
		list_of_head_text=[]
		list_of_head_text=list()
		list_of_text=[]
		list_of_text=list()
		list_of_dates=[]
		list_of_dates=list()
		#attachment_list = Attachment.objects.values('devid').annotate(devid_count=Count('devid')).filter(devid_count__gt=1).order_by("-date_updated")
		#attachment_list = Attachment.objects.values('devid').distinct()
		#attachment_list = Attachment.objects.order_by("date_updated").values_list('devid', flat=True).distinct()
		attachment_list = Attachment.objects.order_by("date_updated")
    #.distinct('devid').values_list('devid', flat=True)
		for row_data in attachment_list:
			list_of_head_text.append(row_data.head_text)
			list_of_dates.append(row_data.date_updated)
			list_of_text.append(row_data.text_update)
			print row_data.text_update
		return render_to_response('developer_panel.html',{'name':uname,'lists':list_of_text,'mydate':list_of_dates},context_instance=RequestContext(request))
	else:
		try:
			print "in post"
			head_text=request.POST.get("caption")
			text=request.POST.get("info")
			print text
			try:
				files=request.FILES.getlist('fileinput')
				print "files taken"
				if(files==""):
					print "in if"
					Attachment.objects.create(devid=mailid,head_text=head_text,text_update=text,file_name="",attachment="",date_updated=datetime.datetime.today())	
				else:
					print "in else"
					print str(files)
					for a_file in files:
						print "in for"
						Attachment.objects.create(devid=mailid,head_text=head_text,text_update=text,file_name=a_file.name,attachment=a_file,date_updated=datetime.datetime.today())	
					return HttpResponseRedirect('/developer_panel/')
			except Exception,e:
				print str(e)
				Attachment.objects.create(dev_id=mailid,text_update=text,file_name="",attachment="",date_updated=datetime.datetime.today())	
		except Exception,e:
			print str(e)
			return render(request,"developer_panel.html",{'name':uname})



@csrf_exempt
def developer_login(request):
	if request.method=='GET':
		return render(request,"developer_login.html",{})		
	else:
		try:
			username=request.POST.get("username")
			password=request.POST.get("password")
			try:
				query=developer_data.objects.get(email=str(username),password=str(password))
				
				if query is None:
					return render(request,"developer_login.html",{})			
				else:
					uname=getattr(query,'name')
					request.session['uname']=uname
					request.session['mailid']=username
					print uname
					print "data valid"
					return HttpResponseRedirect('/developer_panel/')					
			except Exception,e:
				print str(e)
				return render(request,"developer_login.html",{})			
		except Exception,e:
			print "failed to post"
			return render(request,"developer_login.html",{})	
			
		

@csrf_exempt
def send_otp_mail_save_client(name,number,emails,project_id,project_deadline):
	
	rand = random.randint(1000,9999)
	client_password=get_random_string(length=6, allowed_chars='ABCxyz1234567')
	
	email=EmailMessage('Code Nicely Username and Password to log in','Username: '+str(emails)+'and Password: '+str(client_password),to=[emails])
	email.send()


	authkey = "125195AvX4LUlVf57dcd941"
	mobiles = str(number)
	message = "Dear " +str(name)+", welcome to CODENICELY this is your Username and Password for logging in: "+str(emails)+" and "+str(client_password)+"."
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
	
	output = response.read()
	 # Get Response
	return client_password



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