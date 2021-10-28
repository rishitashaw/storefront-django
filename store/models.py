from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, primary_key=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBER_CHOICES = [
        (MEMBERSHIP_BRONZE, 'BRONZE'),
        (MEMBERSHIP_SILVER, 'SILVER'),
        (MEMBERSHIP_GOLD, 'GOLD'),

    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBER_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'PENDING'),
        (PAYMENT_COMPLETE, 'COMPLETE'),
        (PAYMENT_FAILED, 'FAILED'),
    ]

    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, primary_key=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, primary_key=True)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=3)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, primary_key=True)
