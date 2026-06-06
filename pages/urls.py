from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('room/<int:room_id>/', views.room_list, name='room_list'),
    path('logout/', views.logout_view, name='logout'),
    
    # --- PCs ---
    path('add-pc/', views.add_pc, name='add_pc'),
    path('update-pc/<int:pc_id>/', views.update_pc, name='update_pc'),
    path('delete_pc/<int:pc_id>/', views.delete_pc, name='delete_pc'),
    path('get_next_pc_id/', views.get_next_pc_id, name='get_next_pc_id'),
    
    # --- Rooms ---
    path('add_room/', views.add_room, name='add_room'),
    path('edit-room/<int:room_id>/', views.edit_room, name='edit_room'),
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),

    # --- Master List & Borrowing ---
    path('master-list/', views.master_list, name='master_list'),
    path('borrow-item/', views.borrow_item, name='borrow_item'),
    path('return-item/<str:item_type>/<int:item_id>/', views.return_item, name='return_item'),
    path('batch-borrow/', views.batch_borrow, name='batch_borrow'),
    path('batch-return/', views.batch_return, name='batch_return'),
    path('reprint-receipt/<str:batch_id>/', views.reprint_receipt, name='reprint_receipt'),
    path('generate-borrower-slip/<str:batch_id>/', views.generate_borrower_slip, name='generate_borrower_slip'),
    path('generate-word-doc/<str:batch_id>/', views.generate_word_doc, name='generate_word_doc'),
    path('edit-pc-room/<int:pc_id>/', views.edit_pc_room, name='edit_pc_room'),

    # --- Assets & Office Supplies ---
    path('manage-tools/', views.manage_tools, name='manage_tools'),
    path('manage-office-supplies/', views.manage_office_supplies, name='manage_office_supplies'), 
    path('add-tool/', views.add_tool, name='add_tool'), # <--- Added this back so Add Supply works!
    path('edit-tool/<int:tool_id>/', views.edit_tool, name='edit_tool'),
    path('delete-tool/<int:tool_id>/', views.delete_tool, name='delete_tool'),

    # --- Laptops ---
    path('laptops/', views.manage_laptops, name='manage_laptops'),
    path('laptops/add/', views.add_laptop, name='add_laptop'),
    path('laptops/edit/<int:laptop_id>/', views.edit_laptop, name='edit_laptop'),
    path('laptops/delete/<int:laptop_id>/', views.delete_laptop, name='delete_laptop'),
    path('get_next_laptop_id/', views.get_next_laptop_id, name='get_next_laptop_id'),

    path('reactivate-tool/<int:tool_id>/', views.reactivate_tool, name='reactivate_tool'),
]