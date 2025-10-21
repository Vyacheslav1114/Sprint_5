import random
import string

def generate_email(first='vyacheslav', last='migal', cohort='32'):
    """Возвращает уникальный email формата: name_surname_cohort_114@yandex.ru"""
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{first}_{last}_{cohort}_{digits}@yandex.ru"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
