from dataclasses import fields
from rest_framework import serializers
from .models import *

class memoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ('id', 'userID', 'book', 'cardColor', 'chapter', 'createdAt', 'memo', 'textColor', 'verses')
