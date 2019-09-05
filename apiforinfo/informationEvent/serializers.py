from rest_framework import serializers

from informationEvent import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #password에 대한 문제가 생길 수 있기때문에 extra_kwargs를 생성.
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        #how to create a new user profile.
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
     """Serializes profile feed items"""

     class Meta:
         model = models.ProfileFeedItem
         fields = ('id', 'user_profile', 'status_text', 'created_on')
         extra_kwargs = {'user_profile':{'read_only':True }}



