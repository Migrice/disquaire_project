from django.contrib import admin
from .models import Artist, Album, Contact, Booking


admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Contact)
admin.site.register(Booking)


# Register your models here.
