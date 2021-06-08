from rest_framework import serializers

from .models import Score

class ScoreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = [
            'name',
            'points',
        ]