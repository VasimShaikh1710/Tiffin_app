import base64
from django import template
from io import BytesIO

register = template.Library()

@register.filter(name='base64_encode')
def base64_encode(value):
    """Convert image file to base64 encoding"""
    if value:
        try:
            # Open image file and convert it to base64
            with open(value.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            return ''
    return ''
