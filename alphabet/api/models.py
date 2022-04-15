from django.db import models


class History(models.Model):
    """Model to store each request, response, and date/time created in DB
    
    Stores "request" attr as a TextField object to allow for large-sized text 
    storage.
    """

    request = models.TextField(blank = True, default = '')
    response = models.BooleanField(blank = True, default = False)
    created = models.DateTimeField(auto_now_add = True)