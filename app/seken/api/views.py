from datetime import date
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Count
from .models import Newspaper, Word
from .serializers import NewspaperSerializer, WordSerializer, WordRankingSerializer

class NewspaperViewSet(viewsets.ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    http_method_names = ['get']

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    http_method_names = ['get']


class WordRankingViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordRankingSerializer
    http_method_names = ['get']

    def handle_exception(self, exc):
        try:
            return super(self.__class__, self).handle_exception(exc)
        except Exception:
            if len(exc.args) > 0:
                content = {'error': '{}'.format(exc.args[0])}
            else:
                content = {'error': '不明なエラー'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        N = 5
        queryset = Word.objects.all()
        year = self.request.query_params.get('year', None)
        month = self.request.query_params.get('month', None)
        day = self.request.query_params.get('day', None)

        if year and month and day:
            try:
                a_date = date(int(year), int(month),  int(day))
            except ValueError as ex:
                raise ex.__class__("指定した日付に問題があります %s-%s-%s" % (year, month, day))

            try:
                try:
                    num = self.request.query_params.get('num', N)
                    num = int(num)
                except ValueError as ex:
                    raise ex.__class__("numの値は整数で指定する必要があります num: %s" % str(num))
                queryset = queryset.filter(_datetime__date=a_date).values('word').annotate(count=Count('word')).order_by('-count')[:num]
                return queryset
            except ValueError as ex:
                raise ex
        else:
            raise ValueError("year, month, dayパラメータを付与する必要があります")