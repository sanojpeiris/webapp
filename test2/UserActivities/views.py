from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, "invalid information")
            return redirect("/")
    else:
        return render(request, "login.html")


# register command


def register(request):
    if request.method == "POST" and "regular" in request.POST:
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # regular = request.POST["regular"]
        # admin = request.POST["admin"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect("register")

            else:

                # take the objects
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1)
                # save the data to the database
                user.save()
                messages.info(request, "successfully created the Regular user")
                return redirect("/")
        else:
            messages.info(request, "password is not match")
            return redirect("register")
    else:
        if request.method == "POST" and "admin" in request.POST:
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            # regular = request.POST["regular"]
            # admin = request.POST["admin"]

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already taken")
                    return redirect("register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "email exists")
                    return redirect("register")

                else:

                    # take the objects
                    user = User.objects.create_superuser(username=username,
                                                         email=email,
                                                         password=password1)
                    # save the data to the database
                    user.save()
                    messages.info(request, "successfully created the Admin user")
                    return redirect("/")
            else:
                messages.info(request, "password is not match")
                return redirect("/")


def updateUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        user = User.objects.get(username=username)
        user.email = email
        user.save()

        password = User.objects.get(username=username)
        password.set_password(password1)
        password.save()

        messages.info(request, "password changed")
        return redirect("updateUser")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return render(request, "login.html")


def moveToHome(request):
    return render(request, "home.html")


def moveToLogin(request):
    return render(request, "login.html")


def moveToRegister(request):
    return render(request, "register.html")


def moveToUpdateUser(request):
    return render(request, "updateUser.html")


def moveToTodo(request):
    return render(request, "todo.html")
