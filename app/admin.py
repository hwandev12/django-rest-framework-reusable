from django.contrib import admin
from .models import (
    CustomUser,
    Snippet
)

admin.site.register(CustomUser)
admin.site.register(Snippet)