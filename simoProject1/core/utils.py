import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
#					lettere alfabeto          numeri
STRING_LENGTH = 6

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
	return "".join(random.choice(chars) for _ in range(length))

"""
Creazione oggetto su shell da modello Question
per vedere come slung funziona
-----------------------------------------------------------------
(venv) simo@DESKTOP-2A94CQ1:/mnt/c/Users/simop/Desktop/Question_Time/QuestionTime_Project/QuestionTime$ python3.8 manage.py shell
Python 3.8.2 (default, Feb 26 2020, 02:56:10)
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth import get_user_model
>>> custom_user = get_user_model()
>>> u = custom_user.objects.first()
>>> u
<CustomUser: simo>
>>> from questions. models import Question
>>> from questions.models import Question
>>> q = Question.objects.create(author=u, content="prima domanda. funziona?")
>>> q
<Question: prima domanda. funziona?>
>>> q.slug
'prima-domanda-funziona-lbphaz'
>>>  
"""                                                                                                                                                    