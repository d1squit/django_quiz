from django.core.exceptions import ValidationError


def validate_order_num(value):
    if int(value) != value or value < 1 or value > 100:
        raise ValidationError(f"order_num must be integer from 1 to 100")
