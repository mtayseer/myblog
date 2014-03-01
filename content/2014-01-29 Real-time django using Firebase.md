# Real-time django using Firebase

```python
# Mixin to save a django model to Firebase. This enables real-time django
import requests
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core import serializers


class FireBaseModelMixin:
    @staticmethod
    @receiver(post_save)
    def put_in_firebase(sender, instance, created, **kwargs):
        if not isinstance(instance, FireBaseModelMixin):
            return
        object_url = str(instance.__class__.__name__) + '/' + str(instance.id)
        requests.put(settings.FIREBASE_URL_BASE.format(object_url), serializers.serialize('json', [instance]))


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'
```