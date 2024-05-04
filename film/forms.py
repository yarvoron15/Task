from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(
        label="Оценка",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        max_value=10,
        min_value=1
    )
    content = forms.CharField(
        label='Содержание отзыва',
        widget=forms.Textarea(attrs={"class": "form-control"})
    )