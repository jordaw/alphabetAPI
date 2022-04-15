from rest_framework import serializers

from .models import History


class HistorySerializer(serializers.ModelSerializer):
    """Serializer to convert request data to JSON
    
    In order to only prompt the user for the request at 
    localhost:8000/api/alphabet/check, the "response" and "created" attributes 
    of the History object need to be retrieved via the custom get_response() 
    and get_created() methods.

    Meta class fields indicate what fields are converted to JSON and
    subsiquently displayed for each History object on the front end
    """

    # get response attr from History object
    response = serializers.SerializerMethodField('get_response')
    def get_response(self, history_object):
        return history_object.response

    # get created attr from History object
    created = serializers.SerializerMethodField('get_created')
    def get_created(self, history_object):
        return history_object.created

    # all data serialized from request and sent to frontend
    class Meta:
        model = History
        fields = ['id', 'request', 'response', 'created']