from django.contrib import admin
from . models import Cart, Customer, OrderPlaced, Payment, products
# Register your models here

@admin.register(products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity'] 

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','stripe_charge_id','stripe_payment_id','stripe_status','paid'] 

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment'] 