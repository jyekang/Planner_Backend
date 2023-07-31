from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    food = 'food'
    decoration = 'decoration'
    supplies = 'supplies'
    other = 'other'
    EVENT_EXPENSE_CHOICES = (
        (food, 'food'),
        (decoration, 'decoration'),
        (supplies, 'supplies'),
        (other, 'other')
    )
    item_name = models.CharField(max_length=250, choices=EVENT_EXPENSE_CHOICES, default=supplies,)
    custom_item_name = models.CharField(max_length=250, blank=True, null=True)
    amount = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return self.custom_item_name
    
class Attendee(models.Model):
    full_name = models.CharField(max_length=250)
    rsvp = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    assigned_to = models.CharField(max_length=200)

    def __str__(self):
        return self.description
    

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    attendee_id = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='attendee', null=True, blank=True)
    event_name = models.CharField(max_length=100)
    location = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    budget = models.PositiveIntegerField()
    attendees = models.ManyToManyField('Attendee', related_name='events', blank=True)
    tasks = models.ManyToManyField('Task', related_name='events', blank=True)
    expenses = models.ManyToManyField('Expense', related_name='events', blank=True)

    def __str__(self):
        return self.event_name