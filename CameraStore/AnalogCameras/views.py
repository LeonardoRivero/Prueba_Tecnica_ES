from django.shortcuts import render

from .serializers import CameraSerializer, FilmCameraSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets
from .models import Camera, ModelCamera, FilmCamera, Leasing, TechnicalSupport, ItemsCamera, Client
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import json
from datetime import date
import datetime

# Create your views here.
from rest_framework.response import Response


class CRUDCamera(View):

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        try:
            data, created = Camera.objects.get_or_create(**data)
            # if created:
            data_json = json.loads(serialize('json', [data, ]))
            message = "Records Camera Saved Successfully "
            datajson = {"message": message, data._meta.model.__name__: data_json}
            return JsonResponse(datajson, safe=True, status=200)
            # else:
            #     message = "Records Camera Already Existing "
            #     datajson = {"message": message}
            #     return JsonResponse(datajson, safe=True, status=400)
        except Exception as e:
            print(e)
            message = "Error"
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)

    def get(self, request, pk=None):
        if pk:
            data = Camera.objects.filter(id=pk).select_related()
        else:
            data = Camera.objects.all()
        data_json = json.loads(serialize("json", data, use_natural_foreign_keys=True))
        dataJSON = {data.model.__name__: data_json}
        return JsonResponse(dataJSON, safe=True, status=200)

    def put(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            print(data)
            for element in data:
                data_dict = element["fields"]
                Camera.objects.filter(id=pk).update(**data_dict)

            data = Camera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Camera Updated successfully."
            data = {"message": message, "Camera": data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "Camera": []}
            return JsonResponse(data=data, safe=True, status=400)

    def delete(self, request, pk=None):
        try:
            Camera.objects.filter(id=pk).delete()
            data = Camera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Camera deleted."
            data = {"message": message, "data": data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "camera": []}
            return JsonResponse(data=data, safe=True, status=400)


class CRUDModelCamera(View):
    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        try:
            data["camera"] = Camera.objects.get(id=data['camera'])
            data, created = ModelCamera.objects.get_or_create(**data)
            if created:
                data_json = json.loads(serialize('json', [data, ]))
                message = "Records Model Camera Saved Successfully "
                datajson = {"message": message, data._meta.model.__name__: data_json}
                return JsonResponse(datajson, safe=True, status=200)
            else:
                message = "Records Model Camera Already Existing "
                datajson = {"message": message}
                return JsonResponse(datajson, safe=True, status=400)
        except Exception as e:
            print(e)
            message = "Error"
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)

    def get(self, request, pk=None):
        try:
            if pk:
                data = ModelCamera.objects.filter(id=pk).select_related()
            else:
                data = ModelCamera.objects.all()
            data_json = json.loads(serialize("json", data, use_natural_foreign_keys=True))
            dataJSON = {data.model.__name__: data_json}
            return JsonResponse(dataJSON, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "Error . %s " % e
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)

    def put(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            for element in data:
                data_dict = element["fields"]
                data_dict.pop("camera")
                ModelCamera.objects.filter(id=pk).update(**data_dict)

            data = ModelCamera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "ModelCamera Updated successfully."
            data = {"message": message, data.model.__name__: data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "ModelCamera": []}
            return JsonResponse(data=data, safe=True, status=400)


class CRUDFilmCamera(View):

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        try:
            data["camera"] = Camera.objects.get(id=data['camera'])
            record, created = FilmCamera.objects.get_or_create(**data)
            if created:
                data_json = json.loads(serialize('json', [record, ]))
                message = "Records Film Camera Saved Successfully "
                datajson = {"message": message, record._meta.model.__name__: data_json}
                return JsonResponse(datajson, safe=True, status=200)
            else:
                message = "Records Film Camera Already Existing "
                datajson = {"message": message}
                return JsonResponse(datajson, safe=True, status=400)

        except Exception as e:
            print(e)
            message = "Error . %s " % e
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)

    def get(self, request, pk=None):
        if pk:
            data = FilmCamera.objects.filter(id=pk).select_related("camera")
        else:
            data = FilmCamera.objects.all().select_related("camera")
        data_json = json.loads(serialize("json", data, use_natural_foreign_keys=True))
        dataJSON = {data.model.__name__: data_json}
        return JsonResponse(dataJSON, safe=True, status=200)

    def put(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            for element in data:
                data_dict = element["fields"]
                data_dict.pop("camera")
                FilmCamera.objects.filter(id=pk).update(**data_dict)

            data = FilmCamera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Film Camera Updated successfully."
            data = {"message": message, "Film Camera": data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "Film Camera": []}
            return JsonResponse(data=data, safe=True, status=400)

    def delete(self, request, pk=None):
        try:
            FilmCamera.objects.filter(id=pk).delete()
            data = FilmCamera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Film Camera deleted."
            data = {"message": message, "data": data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "FilmCamera": []}
            return JsonResponse(data=data, safe=True, status=400)


class CRUDTechnicalSupport(View):
    def get(self, request, pk=None):
        if pk:
            data = TechnicalSupport.objects.filter(id=pk).select_related()
        else:
            data = TechnicalSupport.objects.all().select_related()
        data_json = json.loads(serialize("json", data, use_natural_foreign_keys=True))
        dataJSON = {data.model.__name__: data_json}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        try:
            data["camera"] = Camera.objects.get(id=data['camera'])
            record, created = TechnicalSupport.objects.get_or_create(**data)
            if created:
                data_json = json.loads(serialize('json', [record, ]))
                message = "Records TechnicalSupport Saved Successfully "
                datajson = {"message": message, record._meta.model.__name__: data_json}
                return JsonResponse(datajson, safe=True, status=200)
            else:
                message = "Records TechnicalSupport Already Existing "
                datajson = {"message": message}
                return JsonResponse(datajson, safe=True, status=400)
        except Exception as e:
            print(e)
            message = "Error . %s " % e
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)

    def put(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            for element in data:
                data_dict = element["fields"]
                data_dict.pop("camera")
                TechnicalSupport.objects.filter(id=pk).update(**data_dict)

            data = TechnicalSupport.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Technical Support Updated successfully."
            data = {"message": message, data.model.__name__: data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "TechnicalSupport": []}
            return JsonResponse(data=data, safe=True, status=400)

    def delete(self, request, pk=None):
        try:
            TechnicalSupport.objects.filter(id=pk).delete()
            data = TechnicalSupport.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "TechnicalSupport deleted."
            data = {"message": message, data.model.__name__: data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "TechnicalSupport": []}
            return JsonResponse(data=data, safe=True, status=400)


class CRUDItemsCamera(View):

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        try:
            data["model"] = ModelCamera.objects.get(id=data['model'])
            data["camera"] = Camera.objects.get(id=data['camera'])
            record, created = ItemsCamera.objects.get_or_create(**data)
            if created:
                data_json = json.loads(serialize('json', [record, ]))
                message = "Records ItemsCamera Saved Successfully "
                datajson = {"message": message, record._meta.model.__name__: data_json}
                return JsonResponse(datajson, safe=True, status=200)
            else:
                message = "Records TechnicalSupport Already Existing "
                datajson = {"message": message}
                return JsonResponse(datajson, safe=True, status=400)
        except:
            message = "Error"
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)

    def get(self, request, pk=None):
        if pk:
            data = ItemsCamera.objects.filter(id=pk).select_related()
        else:
            data = ItemsCamera.objects.all()
        data_json = json.loads(serialize("json", data, use_natural_foreign_keys=True))
        dataJSON = {data.model.__name__: data_json}
        return JsonResponse(dataJSON, safe=True, status=200)

    def put(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            for element in data:
                data_dict = element["fields"]
                data_dict.pop("camera")
                data_dict.pop("model")
                ItemsCamera.objects.filter(id=pk).update(**data_dict)

            data = ItemsCamera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Item for Camera Updated successfully."
            data = {"message": message, "ItemsCamera": data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "ItemsCamera": []}
            return JsonResponse(data=data, safe=True, status=400)

    def delete(self, request, pk=None):
        try:
            ItemsCamera.objects.filter(id=pk).delete()
            data = ItemsCamera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Item for Camera deleted."
            data = {"message": message, "data": data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "ItemsCamera": []}
            return JsonResponse(data=data, safe=True, status=400)


class CRUDClient(View):
    def get(self, request, pk=None):
        if pk:
            data = Client.objects.filter(pk=pk)
        else:
            data = Client.objects.all().order_by("id")
        data_json = json.loads(serialize("json", data, use_natural_foreign_keys=True))
        dataJSON = {data.model.__name__: data_json}
        print(dataJSON)
        return JsonResponse(data=dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            client, created = Client.objects.get_or_create(**data)

            data = Client.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))

            message = "Client created successfully."
            dataJSON = {"message": message, data.model.__name__: data_json}
            return JsonResponse(data=dataJSON, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "client": []}
            return JsonResponse(data=data, safe=True, status=400)

    def put(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            for element in data:
                data_dict = element["fields"]
                Client.objects.filter(id=pk).update(**data_dict)
            message = " Client Edited successfully"
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=200)
        except Exception as e:
            message = e
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)


class CRUDLeasing(View):
    def get(self, request, pk=None):
        if pk:
            data = Leasing.objects.filter(id=pk).select_related()
        else:
            data = Leasing.objects.all()
        data_json = json.loads(serialize("json", data, use_natural_foreign_keys=True))
        dataJSON = {data.model.__name__: data_json}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        try:
            data["itemscamera"] = ItemsCamera.objects.get(id=data['itemscamera'])
            data["client"] = Client.objects.get(id=data['client'])
            print(data)
            record, created = Leasing.objects.get_or_create(**data)
            if created == True:
                data_json = json.loads(serialize('json', [record, ]))
                message = "Records Leasing Saved Successfully "
                datajson = {"message": message, record._meta.model.__name__: data_json}
                return JsonResponse(datajson, safe=True, status=200)
            else:
                message = "Records Leasing Already existing "
                datajson = {"message": message}
                return JsonResponse(datajson, safe=True, status=400)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            datajson = {"message": message, "Leasing": []}
            return JsonResponse(datajson, safe=True, status=400)

    def put(self, request, pk=None):
        try:
            data = json.loads(request.body.decode("utf-8"))
            print(data)
            for element in data:
                data_dict = element["fields"]["itemscamera"]
                ItemsCamera.objects.filter(id=data_dict["id"]).update(**data_dict)
                data_dict = element["fields"]["client"]
                print(data_dict)
                Client.objects.filter(id=data_dict["id"]).update(**data_dict)
                data_dict = element["fields"]
                data_dict.pop("itemscamera")
                data_dict.pop("client")
                Leasing.objects.filter(id=pk).update(**data_dict)

            message = " Leasing Updated successfully"
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=200)
        except Exception as e:
            message = e
            datajson = {"message": message}
            return JsonResponse(datajson, safe=True, status=400)

    def delete(self, request, pk=None):
        try:
            Leasing.objects.filter(id=pk).delete()
            data = ItemsCamera.objects.all().order_by("id")
            data_json = json.loads(serialize("json", data))
            message = "Leasing deleted."
            data = {"message": message, "data": data_json}
            return JsonResponse(data=data, safe=True, status=200)
        except Exception as e:
            print(e)
            message = "An error has occurred. %s " % e
            data = {"message": message, "Leasing": []}
            return JsonResponse(data=data, safe=True, status=400)


# class CRUDFilmCamera(viewsets.ViewSet):
#     """[CRUD Film]
#     """

#     def list(self, request):
#         queryset = FilmCamera.objects.all()
#         serializer = FilmCameraSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = FilmCameraSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         print(serializer.errors)
#         return Response(serializer.errors)

#     def retrieve(self, request, pk=None):
#         queryset = FilmCamera.objects.filter(id=pk)
#         serializer = FilmCameraSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         queryset = FilmCamera.objects.get(id=pk)
#         serializer = FilmCameraSerializer(queryset, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def destroy(self, request, pk):
#         queryset = FilmCamera.objects.get(id=pk)
#         queryset.delete()
#         return Response("Register has been deleted")
