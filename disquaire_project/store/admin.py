from django.contrib import admin
from .models import Artist, Album, Contact, Booking
from django.utils.safestring import mark_safe


#admin.site.register(Album)
#admin.site.register(Artist)


class BookingInline(admin.TabularInline): #tabularInligne permet d'afficher les informations sur plusieurs lignes
    readonly_fields=["created_at","contacted","contact","album",] 
    model=Booking
    fieldsets=[
        (None,{'fields':['album','contacted','created_at',]})
    ]
    extra=0 #ne pas afficher de lignes supplementaires
    verbose_name="Reservation"
    verbose_name_plural='Reservations'

    

class AlbumArtistInline(admin.TabularInline):
    model=Album.artists.through
    extra=1
    verbose_name='Disque' #modification du nom de la relation
    verbose_name_plural='Disques'


@admin.register(Contact) #modifier certains parametres dans le panel d'administration
class ContactAdmin(admin.ModelAdmin):
    inlines=[BookingInline,] #informations qui s'affichent sur plusieurs lignes avec des colonnes

    

@admin.register(Artist) #modifier certains parametres dans le panel d'administration
class ContactArtist(admin.ModelAdmin):
    inlines=[AlbumArtistInline,] #informations qui s'affichent sur plusieurs lignes avec des colonnes

@admin.register(Album) #modifier certains parametres dans le panel d'administration
class AlbumAdmin(admin.ModelAdmin):
    search_fields=['reference','title' ,]


@admin.register(Booking) #modifier certains parametres dans le panel d'administration
class BookingAdmin(admin.ModelAdmin):
    readonly_fields=["created_at","contacted","contact","album",] # lecture seule
    list_filter=['created_at','contacted' ,]

    
    
    def album_link(self,booking):
        url="/content"
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))
        #la methode mark_safe indique que le contenu est du html, sans elle la balise 'a' serait consideree coe une chaine de caractere