from django.urls import include, path
from rest_framework_nested import routers
from views import PollsViewSet, PollsDetailsViewSet

router = routers.SimpleRouter()
router.register(r'domains', PollsViewSet)

polls_router = routers.NestedSimpleRouter(router, r'polls', lookup='poll')
polls_router.register(r'poll-router', PollsDetailsViewSet,
                      basename='poll-basenane')


urlpatterns = [
    path('', include(polls_router.urls)),
]
