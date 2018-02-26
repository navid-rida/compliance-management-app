from .models import Branches
from django.forms import ModelForm

class BranchesForm(ModelForm):
    class Meta:
        model = Branches
        fields = ['branch_code', 'branch_name', 'branch_address', 'opening_date']
