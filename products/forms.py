from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    # Extra field: user can type a custom name if not in dropdown
    custom_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Type custom product name…',
            'id': 'id_custom_name',
        })
    )

    class Meta:
        model = Product
        fields = [
            'category','brand','name','custom_name','model_number',
            'price','condition','stock',
            'processor','ram','storage','display',
            'battery','camera','os','connectivity','description','image',
        ]
        widgets = {
            'category':     forms.Select(attrs={'class':'form-control','id':'id_category'}),
            'brand':        forms.Select(attrs={'class':'form-control','id':'id_brand'}),
            'name':         forms.Select(attrs={'class':'form-control','id':'id_name'}),
            'model_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Model number'}),
            'price':        forms.NumberInput(attrs={'class':'form-control','placeholder':'0.00','step':'0.01'}),
            'condition':    forms.Select(attrs={'class':'form-control'}),
            'stock':        forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            'processor':    forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. Apple A17 Pro'}),
            'ram':          forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 8GB'}),
            'storage':      forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 256GB'}),
            'display':      forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 6.7" AMOLED 120Hz'}),
            'battery':      forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 5000mAh'}),
            'camera':       forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 108MP Triple Camera'}),
            'os':           forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. Android 14 / watchOS 11'}),
            'connectivity': forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 5G, Wi-Fi 6E, Bluetooth 5.3'}),
            'description':  forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'Product description…'}),
            'image':        forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Brand and name choices are populated dynamically via JS;
        # set empty choices here so Django doesn't reject the value.
        self.fields['brand'].widget = forms.Select(
            attrs={'class':'form-control','id':'id_brand'},
            choices=[('','— Select Category First —')]
        )
        self.fields['name'].widget = forms.Select(
            attrs={'class':'form-control','id':'id_name'},
            choices=[('','— Select Brand First —')]
        )
        # Make name not required in model form — we validate manually
        self.fields['name'].required = False

    def clean(self):
        cleaned = super().clean()
        custom = cleaned.get('custom_name','').strip()
        selected = cleaned.get('name','').strip()
        # Prefer custom name if provided
        if custom:
            cleaned['name'] = custom
        elif not selected:
            self.add_error('name', 'Please select a product name or type a custom one.')
        return cleaned


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'email', 'address', 'city', 'pincode']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'phone':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit mobile number'}),
            'email':     forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (optional)'}),
            'address':   forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'House no., Street, Area...'}),
            'city':      forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'pincode':   forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PIN Code'}),
        }
