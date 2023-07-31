from rest_framework import serializers
from .models import Event, User, Expense, Attendee, Task

class EventSerializer(serializers.HyperlinkedModelSerializer):
    attendees = serializers.HyperlinkedRelatedField(
        view_name='attendee_detail',
        many=True,
        read_only=True
    )

    attendee_id = serializers.PrimaryKeyRelatedField(
        queryset=Attendee.objects.all(),
        source='attendee'
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
        fields = ('id', 'attendee_id', 'users', 'event_name', 'location', 'date', 'time', 'budget', 'attendees', 'tasks', 'expenses')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'username', 'password')

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    # custom_item_name = serializers.HyperlinkedRelatedField(
    #     view_name='expense_detail',
    #     read_only=True
    # )
    class Meta:
        model = Expense
        fields = ('item_name', 'custom_item_name', 'amount', 'date')

class AttendeeSerializer(serializers.HyperlinkedModelSerializer):
    # full_name = serializers.HyperlinkedRelatedField(
    #     view_name='attendee_detail',
    #     read_only=True
    # )

    class Meta:
        model = Attendee 
        fields = ('id', 'full_name', 'rsvp')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
    

    class Meta:
        model = Task
        fields = ('id', 'user_id', 'user', 'description', 'complete', 'assigned_to')


    
    


