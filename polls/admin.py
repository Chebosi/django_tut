
# Register your models here.
#make poll app modifiable
from django.contrib import admin

from .models import Question

admin.site.register(Question)
