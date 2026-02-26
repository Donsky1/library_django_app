from rest_framework.routers import DefaultRouter

from apps.contrib.api.v1.views import UserViewSet
from apps.library.api.v1.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = router.urls
