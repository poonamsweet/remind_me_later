from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReminderSerializer


@api_view(['POST'])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = request.user
        # Assign the user to the reminder before saving
        serializer.save(user=user)
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
