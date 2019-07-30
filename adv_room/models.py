from django.db import models

# Create your models here.
# // Starting room
# {
#   "room_id": 0,
#   "title": "Room 0",
#   "description": "You are standing in an empty room.",
#   "coordinates": "(60,60)",
#   "players": [],
#   "items": ["small treasure"],
#   "exits": ["n", "s", "e", "w"],
#   "cooldown": 60.0,
#   "errors": [],
#   "messages": []
# }

class Room (models.Model):
    room_id = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    coordX = models.IntegerField()
    coordY = models.IntegerField()
    exitN = models.CharField(max_length=255)
    exitE = models.CharField(max_length=255)
    exitS = models.CharField(max_length=255)
    exitW = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cooldown = models.IntegerField()
    # elevation = models.IntegerField(null=True)
    # terrain = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return 'Room: ' + str(self.room_id)

class Player (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    current_room = models.IntegerField()
    gold = models.IntegerField(default=0)
    inventory = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    errors = models.CharField(max_length=255)
    messages = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
