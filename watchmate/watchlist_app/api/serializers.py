from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model= Movie
        fields = "__all__"
    
    def get_len_name(self,object):
        return len(object.name)
        
    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError("name is too short")
        else:
            return value
        
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("title and dscription not same")
        return data

