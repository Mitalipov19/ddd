from django_filters import FilterSet
from .models import *


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'level': ['exact'],
            'status': ['exact'],
            'created_by': ['exact'],
            'price': ['gt', 'lt']
        }