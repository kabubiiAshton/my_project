from django.contrib import admin
from .models import Election, Candidate, Voter, Vote, Position


# Register your models here.

class CandidateInline(admin.TabularInline):
    model = Candidate
    fk_name = "election"
    extra = 1

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ("title", 'created_by', "start_time", "end_time", "is_active")
    inlines = [CandidateInline]
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name','election')
    search_fields = ('name',)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", 'position',  'updated_by')
    list_filter = ( 'updated_by', 'position')
    search_fields = ('name',)

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','election')
    search_fields = ('full_name','email')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("election", "candidate", 'position', "voter", "cast_at")
    list_filter = ('election', 'position')
    readonly_fields = ("cast_at",)