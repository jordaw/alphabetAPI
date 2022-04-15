import re
import string

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import History
from .serializers import HistorySerializer


class AlphabetAPIView(APIView):
    """Generic APIView to handle GET and POST for History objects

    GET requests return all previous requests.

    POST requests are checked against self.alphabet() to determine if one of every letter is present in the user entered request.
    """

    serializer_class = HistorySerializer

    def get_queryset(self):
        """
        Returns all History objects in DB
        """
        return History.objects.all()

    def get(self, request, *args, **kwargs):
        """Convert to JSON and renders all objects in DB to front end.
    
        Utilizing the get_queryset() method, all objects in the DB are 
        acquired, converted to JSON through the serializer, and rendered.
        
        Obviously this is not scalable for any application larger than this 
        use, but some simple optimizations can easily be made such as grabbing 
        only a specific amount of records, or the records created within the 
        last 24h etc.
        """
        # send all History objects to serializer to convert to JSON
        history = self.get_queryset()
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        """Create a new history object in DB
    
        This creates a new object in the DB, calls the alphabet() function,
        saves the record, and sends the data to the serializer to convert
        to JSON and render.
        """
        # create and save new history object
        new_request = History.objects.create(
            request = request.data["request"],
            response = self.alphabet(request.data["request"]),
        )
        new_request.save()

        # send new object to serializer to convert to JSON
        serializer = HistorySerializer(new_request)
        return Response(serializer.data)

    def alphabet(self, request_string: str) -> bool:
        """Determines if request_string contains all letters of the alphabet
    
        The key to this function is the use of the set data type. Sets do not
        allow for duplicate values, so naturally after removing all numbers
        and special characters from the lower case input string, a comparison
        of two sets will be very fast.

        Params:
            request_string (str): User provided input.

        Returns:
            output (bool): Whether or not request_string contains all letters
                of the alphabet.
        """

        # if length of request is shorter than 26, it cannot contain the entire alphabet
        if len(request_string) < 26:
            return False

        # set object of all lowercase ascii characters for comparison (a-z)
        alphabet = set(string.ascii_lowercase)

        # regex substitute out all numbers and special chars from lower case request
        # convert output to a set to remove duplicates
        request_string = set(re.sub(r'[^a-zA-Z]', '', request_string.lower()))

        # return comparison of both sets
        return alphabet == request_string