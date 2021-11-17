# TestDevSenior

## Instalar pipenv para manejar el ambiente virtual del proyecto
Para instalar pip, simplemente ejecute:

    $ pip install --user pipx
## Una vez que esté pipxlisto en su sistema, continúe instalando Pipenv:

    $ pipx instalar pipenv

## Despues de instalar pipenv, dirijase al directorio donde se encuentra el archivo Pipfile y ejecute:
    $ pipenv install

## Nota:Si el entornno virtual ya está activado, también puede usar 
    $ pipenv sync
#
## Para correr el proyecto, dirijase al directorio donde se encuentra el archio manage.py y ejecute:
    $ python manage.py runserver

## Los endpoints del proyecto son:
    'camera/list/',--> lista todas los registros existentes
    'camera/add/',--> crea un nuevo registro 
    'camera/<int:pk>/edit/',--> edita los detalles del registro seleccionado por el pk
    'camera/<int:pk>/delete/',--> borra el registro seleccionado por el pk
    'filmcamera/list/'
    'filmcamera/add/'
    'filmcamera/<int:pk>/delete/'
    'filmcamera/<int:pk>/edit/'
    'technicalsupport/list/'
    'technicalsupport/add/'
    'technicalsupport/<int:pk>/edit/'
    'technicalsupport/<int:pk>/delete/'
    'itemscamera/list/'
    'itemscamera/add/'
    'itemscamera/<int:pk>/edit/'
    'itemscamera/<int:pk>/delete/'
    'client/add/'
    'client/list/'
    'client/<int:pk>/edit/'
    'client/<int:pk>/delete/
    'leasing/add/'
    'leasing/list/'
    'leasing/<int:pk>/edit/'
    'leasing/<int:pk>/delete/'

## Tambien se anexa en el directorio del proyecto el archivo requirements.txt ,con el fin de hacer posible la instalacion de los paquetes con algun otro gestor de ambientes virtuales