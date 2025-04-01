from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# # Create your views here.
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Welcome to the REGDORA application!")

@login_required
def index(request):
    print("🚀 The index function is running!")  # Confirm execution
    sys.stdout.flush()  # Force log output

    return HttpResponse("Check your console for the log!")


@login_required
def index(request):

    print("=== index() view has been called ===")  # Debug print
    print(f"User: {request.user.username}, Group Family: {group_family}")  # Debug

    # Define the 3 family groups
    admin_groups = {"root", "administrators"}
    authorized_groups = {"users", "PPSO"}
    
    # Default group family
    group_family = "guests"

    # Get user's groups
    user_groups = {group.name for group in request.user.groups.all()}

    # Determine the group family
    if user_groups & admin_groups:
        group_family = "admin"
    elif user_groups & authorized_groups:
        group_family = "authorized"

    print(f"User: {request.user.username}, Group Family: {group_family}")
    print(f"User: {request.user.username}, Group Family: {group_family}")  
    sys.stdout.flush()  # ✅ Force it to appear in the terminal!
    # Pass the variable to the template
    return render(request, "index.html", {"group_family": group_family})

