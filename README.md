# FNShopFR

## Créateur Original

Tout le mérite reviens au créateur original: [gomashio1596](https://github.com/gomashio1596/Fortnite-ShopBot-v2). J'ai traduit les textes, ajouté la police de Fortnite et surtout la possibilité de publier la boutique sur Twitter !

## Bot qui publie la boutique d'objet de Fortnite du jour sur Twitter

Le bot utilise l'api de [FortniteApi.io](https://fortniteapi.io/) pour générer une image de la boutique du jour (shop.jpg), puis la poste sur Twitter avec le texte désiré. 

<p align="center">
    <img src="https://i.imgur.com/8jAPNMZ.jpg" width="650px" draggable="true">
</p>



## Prérequis
Pour une utilisation locale sur son pc :
- [Python](https://www.python.org/downloads/)
- Le fichier "install.bat" devrait normalement installé automatiquement les logiciels suivants, néanmoins si ça ne fonctionne pas :
    - [Requests](http://docs.python-requests.org/en/master/user/install/)
    - [Pillow](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)
    - [Tweepy](https://docs.tweepy.org/en/stable/install.html)
	
Pour une utilisation en ligne (lancer automatiquement le bot à l'heure de la boutique) :
- [Compte Heroku](https://heroku.com)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

## Como usarlo

Abre `configuration.json` en un editor de texto y completa los campos correspondientes. Una vez terminado, guarda el archivo.

- `apiKey`: Esta sección ya no es necesaria rellenarla, puedes dejarla vacía y el programa funcionará.
- `delayStart`: Esta función introducirá un retraso al generador de la imagen. Ponlo a `0` para que empiece automáticamente. Recomendamos tenerlo a `15` para que la API le de tiempo a actualizarse tras un reseteo de Tienda.
- `supportACreator`: Si tienes Código de Creador, puedes ponerlo aquí para que se publique en el Tweet. Si no, déjalo en blanco.
- `twitter`: Pon `enabled` a `false` si no quieres que la imagen de la Tienda sea tweeteada.

Puedes editar las imagenes que se encuentran en `assets/images/` a tu gusto. ¡No cambies las resoluciones si no es necesario! 

Este repositorio se actualizará con nuevas imagenes si hacen falta.

Spanish Fortnite Shop se debe usar en un programador de tareas como [cron](https://en.wikipedia.org/wiki/Cron) en Linux o [z-cron](https://www.z-cron.com/es/) en Windows.

## Comando para iniciar.

```
python itemshop.py
```
o (más en Linux)
```
python3 itemshop.py
```

## Creditos

- Item Shop data provided by [Fortnite-API](https://fortnite-api.com/)
- Burbank font property of [Adobe](https://fonts.adobe.com/fonts/burbank)
- Luckiest Guy font property of [Google](https://fonts.google.com/specimen/Luckiest+Guy)
