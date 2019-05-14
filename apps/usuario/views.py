from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm

import pyrebase
import os
import httplib2
from oauth2client.client import GoogleCredentials


config = {
    "apiKey": "AIzaSyCqlaqdkWsDdYllGOLnf1aXcIslVBZDwas",
    "authDomain": "refugio-c6e35.firebaseapp.com",
    "databaseURL": "https://refugio-c6e35.firebaseio.com",
    "storageBucket": "refugio-c6e35.appspot.com",
    "serviceAccount": os.getcwd() + "/refugio-firebase-adminsdk.json"
}


_FIREBASE_SCOPES = [
    'refugio-c6e35',
    'shamandul@gmail.com']

firebase = pyrebase.initialize_app(config)


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    auth = firebase.auth()
    #user = auth.create_user_with_email_and_password('shamandul@gmail.com', '123456asd')

    #url = auth.send_email_verification(user['idToken'])
    #print('Sucessfully updated user: {0}'.format(url))
    success_url = reverse_lazy('mascota:mascota')


def registro_usuario_proveedores(launch_browser=True):
    from google_auth_oauthlib import flow
    appflow = flow.InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',
        scopes=['https://www.googleapis.com/auth/bigquery'])

    if launch_browser:
        appflow.run_local_server()
    else:
        appflow.run_console()

    credentials = appflow.credentials

    """Provides an authed http object."""
    http = httplib2.Http()
    # Use application default credentials to make the Firebase calls
    # https://firebase.google.com/docs/reference/rest/database/user-auth
    creds = GoogleCredentials.get_application_default().create_scoped(
        _FIREBASE_SCOPES)
    creds.authorize(http)
    print('Sucessfully proveedor oath http: {0}'.format(creds))
    return http
vKaD4uMkRSUR