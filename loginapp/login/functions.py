from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from .models import StandardUser

def authenticate(username, password):
    try:
        # Attempt to retrieve the user from the database based on the provided username
        user = StandardUser.objects.get(username=username)
        
        # Check if user exists and if the password matches
        is_correct = check_password(password, user.password) if user else False
        
        # If user exists and password is correct, return user details
        if is_correct:
            return {
                "username": user.username,
                "email": user.emailid,
                "company": user.company,
                "designation": user.designation
            }
    except ObjectDoesNotExist:
        # If user does not exist or password is incorrect, return None
        pass
    return None

def find_user(username):
    try:
        # Attempt to retrieve the user from the database based on the provided username
        user = StandardUser.objects.get(username=username)
        
        # If user exists, return user details
        return {
            "username": user.username,
            "email": user.emailid
        } if user else None
    except ObjectDoesNotExist:
        # If user does not exist, return None
        return None
