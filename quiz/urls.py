from django.urls import path

from . import views


app_name = "quiz"
urlpatterns = [
    # ex: /quiz/
    path("", views.index, name="index"),
    # all quiz
    path("allquiz/", views.allquiz, name="allquiz"),


    # ex: /quiz/5/
    path("<int:quiz_id>/<str:token>/", views.single_quiz, name="single_quiz"),
    # ex: /quiz/5/3/
    path(
        "q/<int:quiz_id>/<int:question_id>/<str:name>/",
        views.single_question,
        name="single_question",
    ),
    # ex: /quiz/5/3/vote/
    path("<int:quiz_id>/<int:question_id>/<str:name>/vote/", views.vote, name="vote"),
    # ex: /quiz/5/results/
    path("r/<int:quiz_id>/<str:name>/results/", views.results, name="results"),
    # ex: /quiz/create/
    path("create/", views.create_quiz, name="create_quiz"),
    # ex: /quiz/create/7/2/
    path(
        "create/<int:quiz_id>/<int:question_id>/",
        views.create_question,
        name="create_question",
    ),
    path("exam/", views.code_to_exam, name="exam"),
    path("create_exam/", views.create_exam, name="create_exam"),
    path("register_exam/", views.register_exam, name="register_exam"),
    path("update/<int:quiz_id>/<int:question_id>/<str:token>/", views.candidate_update, name="candidate_update"),
    path("report/", views.report, name="report"),

]
