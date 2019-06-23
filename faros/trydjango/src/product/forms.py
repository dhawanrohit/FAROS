from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
    ]


class RawProductForm(forms.Form):
  title       = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder":"Input title"}))
  description = forms.CharField(
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                      "class": "new-class name two",
                                      "placeholder": "Input description",
                                      "id": "my-id-for-textareas",
                                      "rows":8,
                                      "cols":120,


                                    }
                                    )
                                )
  price       = forms.DecimalField(initial=199.99)