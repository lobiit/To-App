from rest_framework import routers
from todos.views import TodoViewset

router = routers.DefaultRouter()
router.register(r'api/todos', TodoViewset, 'todos')

urlpatterns = router.urls
