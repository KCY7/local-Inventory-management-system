from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# --- 1. PERSONAL COMPUTER ---
class PersonalComputer(models.Model):
    custom_id = models.CharField(max_length=50, unique=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    
    STATUS_CHOICES = [('Working', 'Working'), ('Defective', 'Defective'), ('Missing', 'Missing'), ('Condemned', 'Condemned')]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Working')

    # Component Names
    processor = models.CharField(max_length=100, blank=True)
    ram = models.CharField(max_length=50, blank=True)
    storage = models.CharField(max_length=50, blank=True)
    graphics_card = models.CharField(max_length=100, blank=True)
    motherboard = models.CharField(max_length=100, null=True, blank=True)
    psu = models.CharField(max_length=100, null=True, blank=True) # <-- NEW PSU FIELD
    monitor_details = models.CharField(max_length=255, null=True, blank=True)
    avr_details = models.CharField(max_length=255, null=True, blank=True)
    keyboard_details = models.CharField(max_length=255, null=True, blank=True)
    mouse_details = models.CharField(max_length=255, null=True, blank=True)
    
    # Component Serial Numbers
    processor_sn = models.CharField(max_length=100, blank=True, null=True)
    ram_sn = models.CharField(max_length=100, blank=True, null=True)
    storage_sn = models.CharField(max_length=100, blank=True, null=True)
    graphics_card_sn = models.CharField(max_length=100, blank=True, null=True)
    motherboard_sn = models.CharField(max_length=100, blank=True, null=True)
    psu_sn = models.CharField(max_length=100, blank=True, null=True) # <-- NEW PSU S/N FIELD
    monitor_sn = models.CharField(max_length=100, blank=True, null=True)
    avr_sn = models.CharField(max_length=100, blank=True, null=True)
    keyboard_sn = models.CharField(max_length=100, blank=True, null=True)
    mouse_sn = models.CharField(max_length=100, blank=True, null=True)

    # ==========================================
    # NEW: MULTIPLE SLOTS SUPPORT
    # ==========================================
    ram_2 = models.CharField(max_length=50, blank=True, null=True)
    ram_2_sn = models.CharField(max_length=100, blank=True, null=True)
    ram_3 = models.CharField(max_length=50, blank=True, null=True)
    ram_3_sn = models.CharField(max_length=100, blank=True, null=True)
    ram_4 = models.CharField(max_length=50, blank=True, null=True)
    ram_4_sn = models.CharField(max_length=100, blank=True, null=True)

    storage_2 = models.CharField(max_length=50, blank=True, null=True)
    storage_2_sn = models.CharField(max_length=100, blank=True, null=True)
    storage_3 = models.CharField(max_length=50, blank=True, null=True)
    storage_3_sn = models.CharField(max_length=100, blank=True, null=True)
    storage_4 = models.CharField(max_length=50, blank=True, null=True)
    storage_4_sn = models.CharField(max_length=100, blank=True, null=True)

    # NEW: GPU TYPE TOGGLE
    is_igpu = models.BooleanField(default=False)
    # ==========================================
    
    remarks = models.TextField(blank=True, null=True)
    
    has_monitor = models.BooleanField(default=True)
    has_keyboard = models.BooleanField(default=True)
    has_mouse = models.BooleanField(default=True)
    has_vga = models.BooleanField(default=True)
    has_avr = models.BooleanField(default=True)
    has_hdmi = models.BooleanField(default=True)

    # --- Borrowing Fields ---
    is_borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=100, blank=True, null=True)
    borrower_contact = models.CharField(max_length=50, blank=True, null=True)
    borrower_position = models.CharField(max_length=100, null=True, blank=True)
    borrower_email = models.CharField(max_length=100, null=True, blank=True)
    borrower_branch = models.CharField(max_length=100, null=True, blank=True)
    borrower_purpose = models.TextField(null=True, blank=True)
    
    borrow_location = models.CharField(max_length=50, choices=[
        ('In-Campus', 'In-Campus (Room-to-Room)'), 
        ('Outside', 'Outside (External Borrow)'),
        ('Transfer', 'Inter-Campus Transfer') 
    ], blank=True, null=True)
    
    return_date = models.DateField(blank=True, null=True) 
    batch_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.custom_id

# --- 2. LAPTOP MODEL ---
class Laptop(models.Model):
    custom_id = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=PersonalComputer.STATUS_CHOICES, default='Working')
    
    is_borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=100, blank=True, null=True)
    borrower_contact = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    borrower_position = models.CharField(max_length=100, null=True, blank=True)
    borrower_email = models.CharField(max_length=100, null=True, blank=True)
    borrower_branch = models.CharField(max_length=100, null=True, blank=True)
    borrower_purpose = models.TextField(null=True, blank=True)
    
    borrow_location = models.CharField(max_length=50, choices=[
        ('In-Campus', 'In-Campus (Room-to-Room)'), 
        ('Outside', 'Outside (External Borrow)'),
        ('Transfer', 'Inter-Campus Transfer') 
    ], blank=True, null=True)
    
    return_date = models.DateField(blank=True, null=True)
    batch_id = models.CharField(max_length=100, blank=True, null=True)
    processor = models.CharField(max_length=100, blank=True, null=True, default="-")
    ram = models.CharField(max_length=50, blank=True, null=True, default="-")
    storage = models.CharField(max_length=50, blank=True, null=True, default="-")
    has_charger = models.BooleanField(default=True, verbose_name="Original Charger / Power Adapter")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.custom_id})"

# --- 3. TOOL / ASSET MODEL ---
class Tool(models.Model):
    # Categories for sorting
    CATEGORY_CHOICES = [
        ('Hand Tool', 'Hand Tool'),           
        ('Consumable', 'Consumable'),         
        ('Accessory', 'Accessory'),           
        ('Computer Part', 'Computer Part'),   
        ('Network', 'Network Equipment'),   
        ('Office Supplies', 'Office Supplies'),
        ('Animation', 'Animation'),
        ('Other', 'Other'),     
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Hand Tool')
    quantity = models.IntegerField(default=1)
    
    # ==========================================
    # NEW: UNIT OF MEASURE
    # ==========================================
    UNIT_CHOICES = [
        ('pcs', 'Pieces / Individuals'),
        ('box', 'Box(es)'),
        ('ream', 'Ream(s)'),
        ('pack', 'Pack(s)'),
        ('roll', 'Roll(s)'),
        ('bottle', 'Bottle(s)'),
        ('set', 'Set(s)'),
    ]
    unit_of_measure = models.CharField(max_length=20, choices=UNIT_CHOICES, default='pcs')
    # ==========================================

    status = models.CharField(max_length=50, choices=PersonalComputer.STATUS_CHOICES, default='Working')
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True)
    
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    
    linked_pc = models.ForeignKey('PersonalComputer', on_delete=models.SET_NULL, null=True, blank=True, related_name='components')

    is_borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=100, blank=True, null=True)
    borrower_contact = models.CharField(max_length=50, blank=True, null=True)
    
    borrow_location = models.CharField(max_length=50, choices=[
        ('In-Campus', 'In-Campus (Room-to-Room)'), 
        ('Outside', 'Outside (External Borrow)'),
        ('Transfer', 'Inter-Campus Transfer') 
    ], blank=True, null=True)
    
    return_date = models.DateField(blank=True, null=True)
    batch_id = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
class BorrowedItem(models.Model):
    tool_asset = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True, blank=True)
    borrower_name = models.CharField(max_length=100)
    borrower_contact = models.CharField(max_length=100, null=True, blank=True)
    borrow_location = models.CharField(max_length=100)
    quantity_borrowed = models.IntegerField(default=1)
    
    date_borrowed = models.DateTimeField(auto_now_add=True)
    return_due_date = models.DateField(null=True, blank=True)
    batch_id = models.CharField(max_length=100, null=True, blank=True) 
    borrower_position = models.CharField(max_length=100, null=True, blank=True)
    borrower_email = models.CharField(max_length=100, null=True, blank=True)
    borrower_branch = models.CharField(max_length=100, null=True, blank=True)
    borrower_purpose = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.quantity_borrowed}x {self.tool_asset.name} - {self.borrower_name}"
    
class TransactionHistory(models.Model):
    ACTION_CHOICES = [
        ('Borrow', 'Borrow'),
        ('Return', 'Return'),
        ('Added', 'Added New Asset'), 
    ]
    
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    item_details = models.CharField(max_length=255) 
    borrower_name = models.CharField(max_length=150, default="N/A")
    batch_id = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        ordering = ['-timestamp'] 
        
    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} | {self.action} | {self.item_details}"