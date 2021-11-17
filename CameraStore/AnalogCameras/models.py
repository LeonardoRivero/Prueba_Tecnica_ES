from django.db import models

# Create your models here.


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=120, unique=True)

    objects = models.Manager()

    def __str__(self):
        return 'Id:%d Mark:%s' % (self.id, self.mark)

    def natural_key(self):
        return ({"id": self.id, "mark": self.mark})


class ModelCamera(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=120, unique=True)
    holderFlash = models.BooleanField()
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name='modelcameras')

    objects = models.Manager()

    def __str__(self):
        return 'Model Camera:%s Holder Camera:%s' % (self.model, self.holderFlash)

    def natural_key(self):
        return ({"id": self.id, "model": self.model, "holderFlash": self.holderFlash})


class FilmCamera(models.Model):
    class Film(models.IntegerChoices):
        Film1 = 50
        Film2 = 100
        Film3 = 200
        Film4 = 400
        Film5 = 800
        Film6 = 1600

    class Format(models.IntegerChoices):
        Format1 = 35
        Format2 = 110
        Format3 = 220

    id = models.AutoField(primary_key=True)
    markFilm = models.CharField(max_length=120)
    sensibility = models.IntegerField(choices=Film.choices, default=Film.Film1)
    formatFilm = models.IntegerField(choices=Format.choices, default=Format.Format1)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return 'Id:%s Mark Film:%s Sensibility:%s Format Film:%s Camera:%s' % (self.id, self.markFilm, self.sensibility, self.formatFilm, self.camera)
    # def natural_key(self):
    #     return ({"id":self.id, "markFilm": self.markFilm, "sensibility": self.sensibility,"formatFilm": self.formatFilm,"camera": self.camera})


class TechnicalSupport(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=120)
    # camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    camera = models.OneToOneField(Camera, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return 'address:%s camera:%s' % (self.address, self.camera)

    def natural_key(self):
        return ({"address": self.address, "camera": self.camera.natural_key})


class ItemsCamera(models.Model):

    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=120)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    status = models.CharField(max_length=120)
    model = models.ForeignKey(ModelCamera, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return 'id:%s reference:%s' % (self.id, self.reference)

    def natural_key(self):
        return ({"id": self.id, "reference": self.reference, "status": self.status})


class Client(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    phone = models.IntegerField()
    punishment = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return 'id:%s name:%s' % (self.id, self.name)

    def natural_key(self):
        return ({"id": self.id, "name": self.name, "phone": self.phone, "punishment": self.punishment})


class Leasing(models.Model):
    id = models.AutoField(primary_key=True)
    itemscamera = models.ForeignKey(ItemsCamera, on_delete=models.CASCADE,)
    date = models.DateField()
    expiration_date = models.DateField()
    client = models.OneToOneField(Client, on_delete=models.CASCADE,)
    camera_returned = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return 'id:%s itemscamera:%s' % (self.id, self.itemscamera)
