#usiamo il signal pre_save per permettere al campo
#slug del modello Question di generare uno slug per
#ogni domanda automaticamente

#pre_save emette un segnale prima che l'istanza venga salvata.

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from articles.models import Article
from core.utils import generate_random_string


# aggiunge automaticamente uno slug
# in base all'articolo
@receiver(pre_save, sender=Article)
def add_slug_to_article(sender, instance, *args, **kwargs):
	if instance and not instance.slug:
		slug = slugify(instance.title)

		random_string = generate_random_string()

		instance.slug = slug + "-" + random_string


#Come si ottengono degli slug unici tra di loro?
#Aggiungendo all'instanza slug una stringa di
#caratteri casuali
# vedi la cartella core,
# si è creato il file utils.py

# poi  abbiamo aggiunto la stringa random_string = generate_random_string()
# e default_app_config nel file __init__ di questa app