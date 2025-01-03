from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES=(("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
                  ("Andhra Pradesh","Andhra Pradesh"),
                  ("Arunachal Pradesh","Arunachal Pradesh"),
                  ("Assam","Assam"),
                  ("Bihar","Bihar"),
                  ("Chandigarh","Chandigarh"),
                  ("Chhattisgarh","Chhattisgarh"),
                  ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
                  ("Daman and Diu","Daman and Diu"),
                  ("Delhi","Delhi"),
                  ("Goa","Goa"),
                  ("Gujarat","Gujarat"),
                  ("Haryana","Haryana"),
                  ("Himachal Pradesh","Himachal Pradesh"),
                  ("Jammu and Kashmir","Jammu and Kashmir"),
                  ("Jharkhand","Jharkhand"),
                  ("Karnataka","Karnataka"),
                  ("Kerala","Kerala"),
                  ("Ladakh","Ladakh"),
                  ("Lakshadweep","Lakshadweep"),
                  ("Madhya Pradesh","Madhya Pradesh"),
                  ("Maharashtra","Maharashtra"),
                  ("Manipur","Manipur"),
                  ("Meghalaya","Meghalaya"),
                  ("Mizoram","Mizoram"),
                  ("Nagaland","Nagaland"),
                  ("Odisha","Odisha"),
                  ("Puducherry","Puducherry"),
                  ("Punjab","Punjab"),
                  ("Rajasthan","Rajasthan"),
                  ("Sikkim","Sikkim"),
                  ("Tamil Nadu","Tamil Nadu"),
                  ("Telangana","Telangana"),
                  ("Tripura","Tripura"),
                  ("Uttar Pradesh","Uttar Pradesh"),
                  ("Uttarakhand","Uttarakhand"),
                  ("West Bengal","West Bengal"),)

CATEGORY_CHOICES=(("ST","Shirts"),
                  ("TS","T-Shirts"),
                  ("JN","Jeans"),
                  ("LR","Lowers"),
                  ("SK","Skirts"),
                  ("SH","Shorts"),
                  ("BS","Base"),
                  ("BH","Blush"),
                  ("LS","Lips"),
                  ("SC","Skincare"),
                  ("SN","Sneakers"),
                  ("HS","Heels"),
                  ("TR","Trainers"),
                  ("BT","Boots"),
                  ("TM","Trimmers"),
                  )
class products(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default="")
    prodapp=models.TextField(default="")
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to="product")
    def _str_(self):
        return self.title
    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES, max_length=100)
    def _str_(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES=(
    ("Accepted","Accepted"),
    ("Packed","Packed"),
    ("On The Way","On The Way"),
    ("Delivered","Delivered"),
    ("Cancel","Cancel"),
    ("Pending","Pending"))
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.FloatField()
    stripe_charge_id=models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_id=models.CharField(max_length=100, blank=True, null=True)
    stripe_status=models.CharField(max_length=100, blank=True, null=True)
    paid=models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default="Pending")
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
