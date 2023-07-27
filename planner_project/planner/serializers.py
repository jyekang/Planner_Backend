from rest_framework import serializers
from .models import Event, User, Expense, Attendee, Task

class EventSerializer(serializers.HyperlinkedModelSerializer):
    attendees = serializers.HyperlinkedRelatedField(
        view_name='attendee_detail',
        many=True,
        read_only=True
    )

    tasks = serializers.HyperlinkedRelatedField(
        view_name='task_detail',
        many=True,
        read_only=True
    )

    expenses = serializers.HyperlinkedRelatedField(
        view_name='expense_detail',
        many=True,
        read_only=True
    )

    users = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Event
        fields = ('id', 'users', 'event_name', 'location', 'date', 'time', 'budget', 'attendees', 'tasks', 'expenses')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )

    class Meta:
        model = User
        fields = ('name', 'email', 'username', 'password')

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    custome_item_name = serializers.HyperlinkedRelatedField(
        view_name='expense_detail',
        read_only=True
    )
    class Meta:
        model = Expense
        fields = ('item_name', 'custom_item_name', 'amount', 'date')

class AttendeeSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.HyperlinkedRelatedField(
        view_name='attendee_detail',
        read_only=True
    )

    class Meta:
        model = Attendee 
        fields = ('full_name', 'rsvp')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    

    class Meta:
        model = Task
        fields = ('user', 'description', 'complete', 'assigned_to')

