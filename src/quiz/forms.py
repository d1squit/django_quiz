from django import forms
from django.core.exceptions import ValidationError

from .models import Choice, Question


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        order_num = cleaned_data.get('order_num')
        exam = cleaned_data.get('exam')
        if exam and order_num is not None:
            num_questions = exam.questions.count()
            if not (1 < order_num <= num_questions <= 100):
                raise ValidationError('order_num must be between 1 and the number of questions in the exam and less then 100')
        return cleaned_data


class QuestionInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        print(self.instance.exam)
        if self.instance.exam is not None:
            num_questions = self.instance.exam.questions.count()
            if not (self.instance.MIN_ORDER_NUM <= self.instance.order_num <= num_questions <= self.instance.MAX_ORDER_NUM):
                raise ValidationError(
                    f'order_num must be in range (1, question_count < 100)'
                )

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
