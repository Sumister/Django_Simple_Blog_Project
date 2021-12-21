from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post


# For Home
def home(request):
    return render(request, 'home/home.html')


# For About Page
def about(request):
    return render(request, 'home/about.html')


# For Contact Page
def contact_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been Successfully sent!")
    return render(request, 'home/contact.html')


# For Search
def search(request):
    query = request.GET['query']
    if len(query) > 80:
        all_posts = Post.objects.none()
    else:
        all_posts_title = Post.objects.filter(title__icontains=query)
        all_posts_content = Post.objects.filter(content__icontains=query)
        all_posts = all_posts_title.union(all_posts_content)

    if all_posts.count() == 0:
        messages.warning(request, "No Search Results Found. Please Refine Your queries")
    params = {'all_posts': all_posts, 'query': query}
    return render(request, 'home/search.html', params)


# For Handling Signup
def handle_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check For error inputs

        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "username should only contain letters and numbers")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "passwords do not match")
            return redirect('home')

        # Create a User
        my_user = User.objects.create_user(username=username, email=email, password=pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.success(request, "Your WeCoder Account has been Successfully Created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')


# For Handling Login
def handle_login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try again")
            return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


# For Handling Logout
def handle_logout(request):
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect('home')



