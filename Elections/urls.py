from django.urls import path
from . import views

app_name = 'Election'


urlpatterns = [
    # path("", views.list_elections, name="list"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("<int:pk>/details/", views.election_detail, name="detail"),
    path('create/', views.create_election, name='create'),
    path('positions/create/', views.create_position, name='create_position'),
    path('candidates/add/', views.add_candidate, name='add_candidate'),
    path('<int:election_id>/vote/', views.vote_page, name='vote_page'),
    path("elections/<int:election_id>/delete/", views.delete_election, name="delete_election"),
    path("voters/add/", views.add_voter, name="add_voters"),
    path("voters/import/", views.import_voters, name="import_voters"),
    path("candidates/manage/", views.manage_candidates, name="manage_candidates"),
    path("<int:election_id>/results/", views.results, name="results"),
path("voters/<int:voter_id>/delete/", views.delete_voter, name="delete_voter"),
path(
    "voters/election/<int:election_id>/delete-all/",
    views.delete_all_voters,
    name="delete_all_voters"
),

]
