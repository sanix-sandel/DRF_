from .models import*
from .serializers import *
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter

class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'
    filter_fields=('name',)
    search_fields=('^name',)
    ordering_fields=('name',)


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    filter_backends=[filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filter_fields=(
        'name',
        'game_category',
        'release_date',
        'played',
        #'owner',
    )
    ordering_fields=[
        'name', 
        'release_date'
    ]
    search_fields=[
        '$name'
    ]

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'

    filter_fields=(
        'name',
        'gender',
    )
    search_fields=(
        '^name',
    )
    ordering_fields=(
        'name',
    )


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


#filter
#class PlayerScoreFilter(filters.FilterSet):
##    min_score=NumberFilter(
#        name='score', lookup_expr='gte'
#    )
#    max_score = NumberFilter(name='score', lookup_expr='lte')
#    from_score_date = DateTimeFilter(name='score_date', lookup_expr='gte')
#    to_score_date = DateTimeFilter(name='score_date', lookup_expr='lte')
#   player_name = AllValuesFilter(name='player__name')
#    game_name = AllValuesFilter(name='game__name')#
#
 #   class Meta:
  #      model = PlayerScore
  #      fields = (
  #          'score',
  #          'from_score_date',
  #          'to_score_date',
  #          'min_score',
  #          'max_score',
   #         #player__name will be accessed as player_name
   #         'player_name',
   #         #game__name will be accessed as game_name
   #         'game_name',
    #    )



class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'
    """filter_class=PlayerScoreFilter
    ordering_fields=(
        'score',
        'score_date',
    )"""


class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'


class ApiRoot(generics.GenericAPIView):
    name='api-root'
    
    def get(self, request, *args, **kwargs):
        return Response(
            {'players':reverse(PlayerList.name, request=request),
            'game-categories':reverse(GameCategoryList.name, request=request),
            'games':reverse(GameList.name, request=request),
            'scores':reverse(PlayerScoreList.name, request=request)    
        })