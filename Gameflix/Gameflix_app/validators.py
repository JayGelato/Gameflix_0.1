from django.core.exceptions import ValidationError


def file_size(value):
    filesize = value.size
    if filesize > 200000000:
        raise ValidationError("Maximum size of file is 200Mb")