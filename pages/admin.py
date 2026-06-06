from django.contrib import admin
from .models import Room, PersonalComputer
from .models import TransactionHistory

# 1. Customize the Header (Make it look official)
admin.site.site_header = "School Inventory Admin"
admin.site.site_title = "Inventory Portal"
admin.site.register(TransactionHistory)
admin.site.index_title = "Welcome to the Inventory Manager"


# 2. Customize the Room List
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',) # Shows the name in the list

# 3. Customize the PC List (The Important Part!)
@admin.register(PersonalComputer)
class PCAdmin(admin.ModelAdmin):
    # Show these columns in the list view
    list_display = ('custom_id', 'room', 'status', 'has_mouse', 'has_keyboard')
    
    # Add a filter sidebar on the right
    list_filter = ('room', 'status')
    
    # Add a search bar at the top
    search_fields = ('custom_id', 'processor')
    
    # Make the list editable directly (Optional cool feature)
    list_editable = ('status', 'room')