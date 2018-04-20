from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users
import bcrypt

def index ( request ):
	#this is coming from project urls and going to localhost
	print "index route is working"
	return render( request, "login_app/index.html")

def login(request):
	
	errors = Users.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		print 'we hit this due to invalid email'
		return redirect( '/')
	
	print '############# we hit success'
	return render(request,'login_app/success.html')
	

def register(request):
	if request.method == 'POST':
		print "we hit register Post"
	errors = Users.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect("/")
		# return redirect('/loggedin'+id)

	else:
		users = Users()
		users.first_name = request.POST['first_name']
		users.last_name = request.POST['last_name']
		users.email = request.POST['email']
		users.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		users.save()
		return redirect('/')





# passW= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

# Users.objects.create(first_name=request.POST['fName'],last_name=request.POST["lName"],email_address=request.POST['email'],password= passW)

	# ['e-mail'] = request.form ['e-mail']
	# ['first_name'] = request.form ['first_name']
	# ['last_name'] = request.form ['last_name']
	# ['password'] = request.form ['password']
	# ['pwordconfirm'] = request.form ['pwordconfirm']
	#if 'user_id' not in request.session:
		# users = Users.objects.all()
		# # user= users[0]
		# # print user
		# print "we almost got to context"
		# context = {
		# 	'users': users,
	 #        # 'first_name':user.first_name,
	 #        # 'last_name':user.last_name,
	 #        # 'email':user.email,
	 #        # 'password':user.password,
	 #        # 'created_at':user.created_at,
	 #        # 'updated_at':user.updated_at,
		# }
		# print context
		# return render(request, "login_app/index.html")

# def index(request):
#     if 'counter' not in request.session:
#         request.session['counter'] = 0
#     request.session['counter'] += 1
#     request.session['random_word'] = get_random_string(length = 14)

#     return render(request, "randomWord/index.html")