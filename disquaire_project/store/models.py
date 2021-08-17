from django.db import models


class Artist(models.Model):
    name = models.CharField( 'nom' ,max_length=200, unique=True)

     #modifier l'affichage dans les classes
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='artiste'

class Contact(models.Model):
    email = models.EmailField('email',max_length=100)
    name = models.CharField('nom',max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='prospect'



class Album(models.Model):
    reference = models.IntegerField('reference',null=True)
    created_at = models.DateTimeField('date de creation',auto_now_add=True)
    available = models.BooleanField('disponible',default=True)
    title = models.CharField('titre',max_length=200)
    picture = models.URLField('URL de l"image',)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title
    

class Booking(models.Model):
    created_at = models.DateTimeField('date d"envoie',auto_now_add=True)
    contacted = models.BooleanField('demande traitée?',default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name
    class Meta:
        verbose_name='reservation'




