from django import forms
from .models import *

class File_Upload_Form(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('dev_id','text_update', 'file_name','attachment','date_updated', )