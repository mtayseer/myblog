Title: Real-time Django using Firebase
Status: draft

Web applications are evolving each day. The hot wave now is real-time web applications. There are many ways to add this to your web application.
Today I'm going to talk about one of these ways: [Firebase](https://www.firebase.com/).

### What is Firebase?


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
        firebase_url = 'https://my-objects.firebaseio.com/{}/{}.json'.format(instance.__class__.__name__, instance.id)
        requests.put(firebase_url, serializers.serialize('json', [instance]))


class Company(models.Model, FireBaseModelMixin):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
```