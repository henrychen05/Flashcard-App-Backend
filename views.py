from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Deck
from .models import Flashcard
from .serializers import DeckSerializer
from .serializers import FlashcardSerializer
from django.http import Http404

# Create your views here.
class DeckCreateView(APIView):
    def post(self, request):
        serializer = DeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        decks = Deck.objects.all()
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data)

class DeckDetailView(APIView):
    def get_object(self, pk):
        try:
            return Deck.objects.get(pk=pk)
        except Deck.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        deck = self.get_object(pk)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)

    def put(self, request, pk):
        deck = self.get_object(pk)
        serializer = DeckSerializer(deck, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        deck = self.get_object(pk)
        serializer = DeckSerializer(deck, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        deck = self.get_object(pk)
        deck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlashcardCreateView(APIView):
    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        flashcards = Flashcard.objects.all()
        serializer = FlashcardSerializer(flashcards, many=True)
        return Response(serializer.data)

class FlashcardDetailView(APIView):
    def get_object(self, pk):
        try:
            return Flashcard.objects.get(pk=pk)
        except Flashcard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        flashcard = self.get_object(pk)
        serializer = FlashcardSerializer(flashcard)
        return Response(serializer.data)

    def put(self, request, pk):
        flashcard = self.get_object(pk)
        serializer = FlashcardSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        flashcard = self.get_object(pk)
        serializer = FlashcardSerializer(flashcard, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flashcard = self.get_object(pk)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
