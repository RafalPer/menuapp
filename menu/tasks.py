from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from .models import Dish
import datetime


@shared_task(bind=True)
def send_mails(self):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    dish_created_obj = Dish.objects.filter(created_at__range=[yesterday, today])
    dish_updated_obj = Dish.objects.filter(updated_at__range=[yesterday, today])
    users = get_user_model().objects.all()
    dish_list = []
    dish_updated_list = []
    for dish in dish_updated_obj:
        dish_updated_list.append(dish.name)
    for dish in dish_created_obj:
        dish_list.append(dish.name)
    for user in users:
        mail_subject = 'MenuApp notification'
        message = f'''
        Newly added Dishes: {", ".join(str(x) for x in dish_list)}
        Recently modified Dishes: {", ".join(str(x) for x in dish_updated_list)}
        '''
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return 'Emails Sent'
