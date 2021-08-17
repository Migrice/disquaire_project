from django.core import paginator # afficher un contenu sur plusieurs pages
from django.shortcuts import render,get_object_or_404
from django import template
from django.http import HttpResponse
from .models import Artist, Album ,Booking,Contact
from django.template import loader
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import ContactForm
from django.db import transaction,IntegrityError


def index(request):
     #affiche les albums disponibles, par ordre de creation en allant du plus recent et seulement 8
    albums=Album.objects.filter(available=True).order_by('-created_at')[:6]
    #formatted_albums=["<li>{}</li>".format(album.title) for album in albums]
    #message="""<ul>{}</ul>""".format("\n".join(formatted_albums))
    #template = loader.get_template('store/base.html')
    context={
        'albums':albums
    }
    return render(request,'store/index.html',context)


def listing(request):
    albums_list=Album.objects.filter(available=True)# affiche tous les albums disponibles
    paginator=Paginator(albums_list,10)# affiche 10 albums par page
    page=request.GET.get('page')#recuper le numero de la page sur laquelle on est
    
    try:
        albums=paginator.page(page)
    except PageNotAnInteger:
        albums=paginator.page(1) #afficher la premiere page
    except EmptyPage:
        albums=paginator.page(paginator.num_pages)
    #formatted_albums=["<li>{}</li>".format(album.title) for album in albums]
    #message="""<ul>{}</ul>""".format("\n".join(formatted_albums))
    context={
        'albums':albums
    }
    return render(request,'store/listing.html',context)


def detail(request,album_id):
    '''présent, utilisez la classe du formulaire pour générer
     les champs automatiquement dans le gabarit. Commencez par créer une
      instance de ContactForm() dans la vue puis utilisez-la dans le gabarit'''

    album=get_object_or_404(Album, pk=album_id)#recuperer les données d'un album a travers son id
    artists_name =" ".join([artist.name for artist in album.artists.all()])
    context={
        'album_title':album.title,
        'artists_name':artists_name,
        'album_id':album.id,
        'thumbnail':album.picture
    }
    if request.method == 'POST':
        form=ContactForm( request.POST)
        '''La méthode is_valid() convertit également les valeurs envoyées par l'utilisateur 
        en objet Python. Par exemple, si vous demandez à l'utilisateur d'entrer un chiffre
        et que cela figure dans la classe de formulaire, il sera disponible dans cleaned_data sous la forme d'un entier (int).'''
        if form.is_valid():


           # email=request.POST.get('email') #recuperation des données
            email=form.cleaned_data['email']
            name =form.cleaned_data['name']

            try:

                with transaction.atomic():

                    contact= Contact.objects.filter(email=email) #creation du contact   
                    if not contact.exists():

                        # si le contact n'est pas enregistré il cree un nouveau
                        contact=Contact.objects.create(
                            email = email,
                            name = name
                        )
                    else:
                        contact=contact.first()

                    album=get_object_or_404(Album,id=album_id)

                    booking=Booking.objects.create(
                        contact=contact,
                        album=album
                    )
                
                    album.available=False 
                    album.save()
                    context={
                        'album_title':album.title

                    }
                    return render(request,'store/merci.html',context)
            except IntegrityError:
                form.errors['internal']="une erreur interne est apparue. Merci de recommencer votre requete"


        
            
    else:
        form= ContactForm()
    context['form']=form
    context['errors']=form.errors.items()
    
    print (context)
    return render(request, 'store/detail.html', context)


def search(request):
    
    query = request.GET.get('query')
    if not query:
        albums=Album.objects.all()#affiche tous les albums si rien n'est entré
    else:
        albums=Album.objects.filter(title__icontains=query) # recupere les titres sans tenir compte de la casse
        if not albums.exists() :
           albums=Album.objects.filter(artists__name__icontains=query)# rechercher un album a travers l'artiste
        
    title="Resultats pour la requete %s"%query
    context={
        'albums':albums,
        'title':title
    }        

    return render(request, 'store/search.html',context)