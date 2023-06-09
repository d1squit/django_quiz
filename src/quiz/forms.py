from django import forms
from django.core.exceptions import ValidationError

from .models import Choice, Question


class QuestionInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        order = list(map(lambda item: item.cleaned_data['order_num'], self.forms))

        for order_num in order:
            if not (1 <= order_num <= len(self.forms) <= self.instance.QUESTION_MAX_LIMIT):
                raise ValidationError('order_num must be in range (1, question_count < 100)')

        if sum(order) != sum(set(order)):
            raise ValidationError('order_num must increase on 1')

        if not (self.instance.QUESTION_MIN_LIMIT <= len(self.forms) <= self.instance.QUESTION_MAX_LIMIT):
            raise ValidationError(
                f'Questions count must be range '
                f'from {self.instance.QUESTION_MIN_LIMIT} '
                f'to {self.instance.QUESTION_MAX_LIMIT} inclusive'
            )


class ChoiceInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        num_correct_answers = sum(form.cleaned_data['is_correct'] for form in self.forms)

        if num_correct_answers == 0:
            raise ValidationError('You must select at least 1 option.')

        if num_correct_answers == len(self.forms):
            raise ValidationError('NOT allowed to select all options.')


class ChoiceForm(forms.ModelForm):
    is_selected = forms.BooleanField(required=False)

    class Meta:
        model = Choice
        fields = ['text']


ChoicesFormSet = forms.modelformset_factory(
    model=Choice,
    form=ChoiceForm,
    extra=0
)
