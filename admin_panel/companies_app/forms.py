from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import Department


class ContactForm(forms.Form):
    email = forms.EmailField(label='email',
                             widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={'placeholder': 'Напишите здесь...',
                                                           'class': "form-control rounded-0"}))


class DepartmentForm(forms.ModelForm):
    def __init__(self, new_id, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        # self.fields['parent'].queryset = TreeNodeChoiceField(queryset=Department.objects.all().filter(company=new_id))
        self.fields['parent'].queryset = Department.objects.all().filter(company=new_id)

    # department_name = forms.CharField(label='Название',
    #                                   widget=forms.TextInput(
    #                                       attrs={'placeholder': 'Name', 'class': 'form-control rounded-0'}))

    # q_set_1 = Department.objects.all()
    # print(q_set_1)




    class Meta:
        model = Department
        exclude = ('company',)

