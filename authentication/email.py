from django.core.mail import send_mail
import random
from django.conf import settings
from.models import CustomUser
from .models import OTP


def send_otp_via_email(email):
    subject = "Your Password Reset OTP Verification"
    otp = random.randint(1000, 9999)
    message = f'Your Otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email]) 
    email_user = CustomUser.objects.get(email=email)
    if OTP.objects.filter(user__email=email_user.email).exists():
        OTP.objects.filter(user__email=email_user.email).update(otp=otp)

    else:
        OTP.objects.create(user=email_user, otp=otp)
