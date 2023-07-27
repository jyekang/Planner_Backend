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

    event_url = serializers.ModelSerializer.serializer_url_field(
        view_name='event_detail'
    )

    attendee_url = serializers.ModelSerializer.serializer_url_field(
        view_name='attendee_detail'
    )

    expense_url = serializers.ModelSerializer.serializer_url_field(
        view_name='expense_detail'
    )

    task_url = serializers.ModelSerializer.serializer_url_field(
        view_name='task_detail'
    )



    class Meta:
        model = Event
        fields = ('id', 'event_url', 'attendee_url', 'expense_url', 'task_url', 'users', 'event_name', 'location', 'date', 'time', 'budget', 'attendees', 'tasks', 'expenses')

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


    
    


