from rest_framework.viewsets import ModelViewSet

from apps.quiblet.models import Quiblet

from .permissions import IsRangerOrReadOnly
from .serializers import QuibletSerializer


class QuibletViewSet(ModelViewSet):
    queryset = Quiblet.objects.all()
    serializer_class = QuibletSerializer
    permission_classes = (IsRangerOrReadOnly,)

    def perform_create(self, serializer):
        quibber = self.request.user_profile  # type: ignore
        serializer.save(quibber=quibber)