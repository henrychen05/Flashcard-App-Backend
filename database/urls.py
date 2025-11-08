from django.urls import path
from .views import DeckCreateView, DeckDetailView, FlashcardCreateView, FlashcardDetailView

urlpatterns = [
    path('decks/', DeckCreateView.as_view(), name = 'deck-create'),
    path('decks/<int:pk>/', DeckDetailView.as_view(), name = 'deck-detail'),
    path('flashcards/', FlashcardCreateView.as_view(), name = 'flashcard-create'),
    path('flashcards/<int:pk>/', FlashcardDetailView.as_view(), name = 'flashcard-detail')
]
