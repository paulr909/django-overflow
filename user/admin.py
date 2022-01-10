from django.contrib import admin

from qanda.models import Answer, Question

admin.site.register(Question)
admin.site.register(Answer)
