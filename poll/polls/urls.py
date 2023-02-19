from django.urls import path
from .views import main_page, question_detail, results, votes, results_data

urlpatterns = [
    path('', main_page, name='main_page'),
    path('<int:question_id>/', question_detail, name='question_detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/<str:obj_id>', results_data, name='results_data'),
    path('<int:question_id>/votes/', votes, name='votes'),
]
