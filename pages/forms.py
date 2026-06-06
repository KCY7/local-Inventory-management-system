from django import forms
from .models import PersonalComputer, Tool, Laptop

# --- EXISTING PC FORM ---
class PCForm(forms.ModelForm):
    class Meta:
        model = PersonalComputer
        # Added 'graphics_card' to fields so the widget works
        fields = ['custom_id', 'room', 'status', 'processor', 'ram', 'graphics_card', 'storage', 
                  'has_monitor', 'has_keyboard', 'has_mouse', 'has_avr']
        
        widgets = {
            'custom_id': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. LAB-01'}),
            'room': forms.Select(attrs={'class': 'form-input'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
            'processor': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Intel i5'}),
            'ram': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 8GB'}),
            'graphics_card': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. GTX 1050'}),
            'storage': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 500GB SSD'}),
        }

# --- NEW SMART ASSET FORM ---
class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        # We only need these 4 fields. 
        # The 'Smart Form' Javascript will combine details into the 'name' field.
        fields = ['category', 'name', 'quantity', 'status']
        
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        widgets = {
            # Existing widgets...
            'custom_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. LAP-01'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Dell'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Latitude'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            
            # NEW STYLING FOR SPECS
            'processor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Intel i5'}),
            'ram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 8GB'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 512GB SSD'}),
            
            # CHECKBOX STYLE
            'has_charger': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'width: 20px; height: 20px;'}),
        }