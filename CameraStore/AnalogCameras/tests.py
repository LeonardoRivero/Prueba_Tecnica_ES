from django.shortcuts import resolve_url
from django.test import TestCase
from AnalogCameras.models import Camera, ModelCamera, FilmCamera, TechnicalSupport, ItemsCamera, Client
# from django.test import Client
import json
from django.http import HttpResponse
from django.core.serializers import serialize
import datetime

from AnalogCameras.models import Leasing
from django.core.serializers.json import DjangoJSONEncoder

# Create your tests here.

STATUS_CODE_OK = 200


class CameraTestCase(TestCase):
    def setUp(self):
        self.payload = {"mark": "New"}
        self.payload_updated = {"mark": "New Camera Updated"}
        for i in range(1, 5):
            self.camera = Camera.objects.create(mark='New Camera '+str(i))
        return self.camera

    def test_create_camera(self):
        print("Creating Camera:")
        response = self.client.post(
            "/api/camera/new/", data=json.dumps(self.payload), content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_get_single_camera(self):
        print("Get single Camera")
        response = self.client.get(
            "/api/camera/1/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_get_all_camera(self):
        print("Get all Cameras")
        response = self.client.get(
            "/api/camera/all/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_update_camera(self):
        print("Updating Camera pk=4")
        data_json = json.loads(serialize('json', [self.camera, ]))
        print(data_json)
        for element in data_json:
            element["fields"] = self.payload_updated

        response = self.client.put(
            "/api/camera/4/", data=json.dumps(data_json), content_type='application/json')
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_delete_camera(self):
        print("Deleting Camera pk=2")
        response = self.client.delete("/api/camera/2/", kwargs={'pk': None})
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("Response as Json", response.json())
        print("-"*50)


class FilmCameraTestCase(TestCase):
    def setUp(self):
        self.camera = CameraTestCase.setUp(self)
        self.filmcamera = FilmCamera.objects.create(
            markFilm='New FilmCamera', sensibility=50, formatFilm=35, camera=self.camera)
        self.payload = {"markFilm": 'New FilmCamera',
                        "sensibility": 50, "formatFilm": 35, "camera": 1}
        self.payload_updated = {"markFilm": "New Film Camera Updated",
                                "sensibility": 100, "formatFilm": 50, "camera": 4}
        for i in range(1, 5):
            self.filmcamera = FilmCamera.objects.create(
                markFilm=f'New Film Camera {i}', sensibility=100, formatFilm=110, camera=self.camera)
        return self.filmcamera

    def test_get_all_filmcamera(self):
        print("Get all Film Cameras")
        response = self.client.get(
            "/api/filmcamera/all/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_create_filmcamera(self):
        print("Creating FilmCamera:")
        response = self.client.post("/api/filmcamera/new/", data=json.dumps(self.payload),
                                    content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_update_filmcamera(self):
        print("Updating Film Camera pk=4")
        data_json = json.loads(serialize('json', [self.filmcamera, ]))
        for element in data_json:
            element["fields"] = self.payload_updated
        print(data_json)
        response = self.client.put(
            "/api/filmcamera/4/", data=json.dumps(data_json), content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_delete_film_camera(self):
        print("Deleting Film Camera pk=2")
        response = self.client.delete(
            "/api/filmcamera/2/", kwargs={'pk': None})
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("Response as Json", response.json())
        print("-"*50)


class ModelCameraTestCase(TestCase):
    def setUp(self):
        self.camera = CameraTestCase.setUp(self)
        self.payload = {"model": "New", "holderFlash": True, "camera": 1}
        self.payload_updated = {
            "model": "New Model Camera Updated", "holderFlash": True, "camera": 4}
        for i in range(1, 5):
            self.modelcamera = ModelCamera.objects.create(
                model='New Camera '+str(i), holderFlash=True, camera=self.camera)
        return self.modelcamera

    def test_create_modelcamera(self):
        print("Creating ModelCamera:")
        response = self.client.post("/api/modelcamera/new/", data=json.dumps(self.payload),
                                    content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_get_all_modelcamera(self):
        print("Get all ModelCameras")
        response = self.client.get(
            "/api/modelcamera/all/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)
        return response

    def test_get_single_modelcamera(self):
        print("Get single Model Camera")
        response = self.client.get(
            "/api/modelcamera/1/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)
        return response

    def test_update_modelcamera(self):
        print("Updating Model Camera pk=4")
        data_json = json.loads(serialize('json', [self.modelcamera, ]))
        for element in data_json:
            element["fields"] = self.payload_updated

        response = self.client.put(
            "/api/modelcamera/4/", data=json.dumps(data_json), content_type='application/json')
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)


class TechnicalSupportTestCase(TestCase):
    def setUp(self):
        self.camera = CameraTestCase.setUp(self)
        self.technical_support = TechnicalSupport.objects.create(
            address='New Address Tech Support ', camera=self.camera)
        self.payload = {"address": 'New Address Tech Support ', "camera": 1}
        self.payload_updated = {
            "address": 'New Address Tech Support Updated ', "camera": 1}

    def test_create_technical_support(self):
        print("Creating TechnicalSupport")
        response = self.client.post("/api/technicalsupport/new/", data=json.dumps(self.payload),
                                    content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_get_all_technical_support(self):
        print("Get all Address Technical Support")
        response = self.client.get(
            "/api/technicalsupport/all/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_update_filmcamera(self):
        print("Updating Technical Support pk=1")
        data_json = json.loads(serialize('json', [self.technical_support, ]))
        print(data_json)
        for element in data_json:
            element["fields"] = self.payload_updated

        response = self.client.put(
            "/api/technicalsupport/1/", data=json.dumps(data_json), content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_delete_film_camera(self):
        print("Deleting Technical Support pk=1")
        response = self.client.delete(
            "/api/technicalsupport/1/", kwargs={'pk': None})
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("Response as Json", response.json())
        print("-"*50)


class ItemsCameraTestCase(TestCase):
    def setUp(self):
        self.camera = CameraTestCase.setUp(self)
        self.model = ModelCamera.objects.create(
            model='New Model Camera', holderFlash=True, camera=self.camera)
        self.items_camera = ItemsCamera.objects.create(
            reference='Reference 1', camera=self.camera, status="On Store", model=self.model)

        self.payload = {"reference": 'Reference 1',
                        "camera": 1, "status": "On Store", "model": 1}
        self.payload_updated = {
            "reference": 'Reference 1 Updated', "camera": 1, "status": "On Store", "model": 1}
        return self.items_camera

    def test_get_all_items_camera(self):
        print("Get all Items Camera ")
        response = self.client.get(
            "/api/itemscamera/all/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_create_items_camera(self):
        print("Creating Items Camera")
        response = self.client.post("/api/itemscamera/new/", data=json.dumps(self.payload),
                                    content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_get_single_items_camera(self):
        print("Get single items Camera")
        response = self.client.get(
            "/api/itemscamera/1/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)
        return response

    def test_update_item_camera(self):
        print("Updating Items Camera pk=1")
        data_json = json.loads(serialize('json', [self.items_camera, ]))
        for element in data_json:
            element["fields"] = self.payload_updated
        print(data_json)
        response = self.client.put(
            "/api/itemscamera/1/", data=json.dumps(data_json), content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)

    def test_delete_items_camera(self):
        print("Deleting Film Camera pk=2")
        response = self.client.delete(
            "/api/itemscamera/1/", kwargs={'pk': None})
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("Response as Json", response.json())
        print("-"*50)


class LeasingTestCase(TestCase):
    def setUp(self):
        self.test = datetime.date.today()
        self.ahora = datetime.date.today().isoformat()
        self.clients = Client.objects.create(name='New Client', phone=123123, punishment=False)
        self.clients2 = Client.objects.create(name='Other New Client', phone=123, punishment=False)
        self.item_camera=ItemsCameraTestCase.setUp(self)
        
        self.expiration_date = self.test + datetime.timedelta(days=7)
        self.leasing=Leasing.objects.create(itemscamera=self.item_camera, date=self.ahora,expiration_date=self.ahora, client=self.clients,camera_returned=True)
        self.payload = {"itemscamera": 1,"date":self.ahora , "expiration_date":self.ahora , "client": 2,"camera_returned":True}

    def test_get_all_leasing(self):
        print("Get all Leasing Camera ")
        response = self.client.get("/api/leasing/all/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("-"*50)
    
    def test_delete_leasing(self):
        print("Deleting Film Camera pk=2")
        response = self.client.delete("/api/leasing/1/", kwargs={'pk': None})
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        print("Response as Json", response.json())
        print("-"*50)

    def test_create_leasing(self):
        print("Creating Leasing Camera")
        print(self.clients,self.clients2)
        response = self.client.post("/api/leasing/new/", data=json.dumps(self.payload),content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        # print("-"*50)
