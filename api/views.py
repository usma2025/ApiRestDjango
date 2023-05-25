from django.views import View 
from django.http.response  import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Login,Register,Posts
import json
# Create your views here.
class LoginView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # Metodo Get para obtener los datos de la tabla Login (Se puede consultar por cedula ciudadania o dejandolo vacio para todos los datos)
    def get(self,request,cedulaCiudadania=''):
        '''Filtrar por id'''
        if(cedulaCiudadania!=''):
            login=list(Login.objects.filter(cedulaCiudadania=cedulaCiudadania).values())
            if len(login)>0:
                loginUnit=login[0]
                datos={'message':'Success','login':loginUnit}
            else:
                datos={'message':'Login not found...'}
            return JsonResponse(datos)
        else:
            '''Mostrar todos los datos'''
            login=list(Login.objects.values())
            if len(login)>0:
                datos={'message':'Success','login':login}
            else:
                datos={'message':'Login not found...'}
            return JsonResponse(datos)
    # Metodo Post para agregar datos en este caso hay que especificar mediante el body y un json la cedulaCiudadania, user y password
    def post(self,request):
        jd=json.loads(request.body)
        print(jd)
        '''Contrasena encryptarla validar como hacerlo'''
        Login.objects.create(cedulaCiudadania=jd['cedulaCiudadania'],user=jd['user'],password=jd['password'])
        datos = {'message':'Success'}
        return JsonResponse(datos)
    # Metodo Put para actualizar datos en este caso hay que especificar por la url el valor a actualizar y en el body cambiar los datos necesarios
    def put(self,request,cedulaCiudadania=''):
        '''Validar Id por CedulaCiudania'''
        jd=json.loads(request.body)
        login=list(Login.objects.filter(cedulaCiudadania=cedulaCiudadania).values())
        if len(login)>0:
            loginUnit=Login.objects.get(cedulaCiudadania=cedulaCiudadania)
            loginUnit.user=jd['user']
            loginUnit.password=jd['password']
            loginUnit.save()
            datos = {'message':'Success'}
        else:
            datos={'message':'Login not found...'}
        return JsonResponse(datos)
    # Metodo Delete para eliminar datos en este caso hay que especificar en la url el valor a eliminar
    def delete(self,request,cedulaCiudadania=''):
        login=list(Login.objects.filter(cedulaCiudadania=cedulaCiudadania).values())
        if len(login) > 0:
            Login.objects.filter(cedulaCiudadania=cedulaCiudadania).delete()
            datos = {'message':'Success'}
        else:
            datos={'message':'Login not found...'}
        return JsonResponse(datos)
        


class RegisterView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # Metodo Get para obtener los datos de la tabla Register (Se puede consultar por cedula ciudadania o dejandolo vacio para todos los datos)
    def get(self,request, cedulaCiudadania_id=''):
        if(cedulaCiudadania_id!=''):
            register=list(Register.objects.filter(cedulaCiudadania_id=cedulaCiudadania_id).values())
            if len(register)>0:
                registerUnit=register[0]
                datos={'message':'Sucess','Register':registerUnit}
            else:
                datos={'message':'Register not found...'}
            return JsonResponse(datos)
        else:
            register=list(Register.objects.values())
            if len(register)>0:
                datos={'message':'Sucess','Register':register}
            else:
                datos={'message':'Register not found...'}
            return JsonResponse(datos)
    # Metodo Post para agregar datos en este caso hay que especificar mediante el body y un json la cedulaCiudadania, name, lastName, birthday y gender
    def post(self,request):
        jd=json.loads(request.body)
        print(jd)

        Register.objects.create(cedulaCiudadania_id=jd['cedulaCiudadania_id'],name=jd['name'],lastName=jd['lastName'],birthday=jd['birthday'],gender=jd['gender'])
        datos = {'message':'Sucess'}
        return JsonResponse(datos)
    # Metodo Put para actualizar datos en este caso hay que especificar por la url el valor a actualizar y en el body cambiar los datos necesarios   
    def put(self,request,cedulaCiudadania_id=''):
        jd=json.loads(request.body)
        register=list(Register.objects.filter(cedulaCiudadania_id=cedulaCiudadania_id).values())
        if len(register)>0:
            registerUnit=Register.objects.get(cedulaCiudadania_id=cedulaCiudadania_id)
            registerUnit.name = jd['name']
            registerUnit.lastName = jd['lastName']
            registerUnit.birthday = jd['birthday']
            registerUnit.gender = jd['gender']
            registerUnit.save()
            datos = {'message':'Sucess'}
        else:
            datos={'message':'Register not found...'}
        return JsonResponse(datos)


    # Metodo Delete para eliminar datos en este caso hay que especificar en la url el valor a eliminar        
    def delete(self,request,cedulaCiudadania_id=''):
        register=list(Register.objects.filter(cedulaCiudadania_id=cedulaCiudadania_id).values())
        if len(register)>0:
            Register.objects.filter(cedulaCiudadania_id=cedulaCiudadania_id).delete()
            datos = {'message':'Sucess'}
        else:
            datos={'message':'Register not found...'}
        return JsonResponse(datos)
        
class PostsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    # Metodo Get para obtener los datos de la tabla Register (Se puede consultar por Id o dejandolo vacio para todos los datos)
    def get(self,request, id=0):
        if(id>=0):
            posts=list(Posts.objects.filter(id=id).values())
            if len(posts)>0:
                postsUnit=posts[0]
                datos={'message':'Sucess','Posts':postsUnit}
            else:
                datos={'message':'Posts not found...'}
            return JsonResponse(datos)
        else:
            posts=list(Posts.objects.values())
            if len(posts)>0:
                datos={'message':'Sucess','Posts':posts}
            else:
                datos={'message':'Posts not found...'}
            return JsonResponse(datos)
    # Metodo Post para agregar datos en este caso hay que especificar mediante el body y un json el user, description e images
    def post(self,request):
        jd=json.loads(request.body)
        print(jd)

        Posts.objects.create(user_id=jd['user_id'],description=jd['description'],images=jd['images'],date=jd['date'])
        datos = {'message':'Sucess'}
        return JsonResponse(datos)
    # Metodo Put para actualizar datos en este caso hay que especificar por la url el valor a actualizar y en el body cambiar los datos necesarios   
    def put(self,request, id=0):
        jd=json.loads(request.body)
        posts=list(Posts.objects.filter(id=id).values())
        if len(posts)>0:
            postsUnit=Posts.objects.get(id=id)
            postsUnit.description = jd['description']
            postsUnit.images = jd['images']
            postsUnit.date = jd['date']
            postsUnit.save()
            datos = {'message':'Sucess'}
        else:
            datos={'message':'Register not found...'}
        return JsonResponse(datos)
    # Metodo Delete para eliminar datos en este caso hay que especificar en la url el valor a eliminar        
    def delete(self,request,id=0):
        posts=list(Posts.objects.filter(id=id).values())
        if len(posts)>0:
            Posts.objects.filter(id=id).delete()
            datos = {'message':'Sucess'}
        else:
            datos={'message':'Register not found...'}
        return JsonResponse(datos)
