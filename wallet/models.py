# from tkinter import CASCADE
from distutils.command.upload import upload
from django.db import models
 #Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length= 20,null=True)
    last_name = models.CharField(max_length= 20,null=True)
    address = models.CharField(max_length= 15)
    email = models.EmailField()
    phone_number = models.CharField(max_length= 15,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length= 15,choices= GENDER_CHOICES,null=True)
    age = models.PositiveBigIntegerField()
    id_number = models.CharField(max_length= 15,null=True)
    nationality = models.CharField(max_length= 15,null=True)
    profile_picture = models.ImageField(upload_to= 'profile_picture/',null=True)

class Wallet(models.Model):
    User_id = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    Amount = models.IntegerField()
    time = models.DateTimeField(null=True)
    # transaction = models.ForeignKey("Transaction",on_delete= models.CASCADE, related_name= "wallet_transaction")
    status = models.CharField(max_length= 15,null=True)
    history = models.DateTimeField()
    pin = models.CharField(max_length= 15,null=True)

class Account(models.Model):
    account_name = models.CharField(max_length= 15,null=True)
    account_number = models.IntegerField(null=True)
    ACCOUNTTYPE_CHOICES = (
        ('W', 'Withdrawal'),
        ('S', 'Savings'),
        ('D', 'Deposits'),
    )
    account_type = models.CharField(max_length= 15, choices= ACCOUNTTYPE_CHOICES, null=True)
    balance = models.IntegerField()
    wallet = models.ForeignKey("Wallet",on_delete= models.CASCADE, related_name= "account_wallet",null=True)
    

class Transaction(models.Model):
    transaction_code = models.CharField(max_length= 15,null=True)
    wallet_one = models.ForeignKey("Wallet",on_delete= models.CASCADE,related_name="Transaction_wallet", null=True)
    transaction_amount = models.IntegerField()
    transaction_number = models.IntegerField(null=True)  
    TRASACTION_TYPE_CHOICES = (
        ('D','Debit'),
        ('C','Credit'),
    )
    transaction_type = models.CharField(max_length= 15, choices= TRASACTION_TYPE_CHOICES, null=True)   #
    transaction_fee = models.IntegerField()
    transaction_time = models.DateField(null=True)
    # transaction_receipt = models.ForeignKey("Receipt",on_delete= models.CASCADE,related_name="transaction_transaction_receipt")  
    origin_account = models.ForeignKey("Account",on_delete= models.CASCADE,related_name="transaction_origin", null=True)
    destination_account = models.ForeignKey("Account",on_delete= models.CASCADE, related_name= "transaction_destination", null=True)

class Card(models.Model):
    card_name = models.CharField(max_length= 15,null=True)
    card_number = models.IntegerField()
    CARD_TYPE_CHOICES = (
        ('C','Credit card'),
        ('D','Debit card'),
    )
    card_type = models.CharField(max_length= 15, choices= CARD_TYPE_CHOICES, null=True)
    cvv_code = models.IntegerField(null=True)
    CARD_ISSUER_CHOICES = (
        ('V','Visa'),
        ('M','Master card'),
    )
    card_issuer = models.CharField(max_length= 15, choices= CARD_ISSUER_CHOICES, null=True)
    date_issued = models.DateTimeField(null=True)
    expiry_date = models.DateTimeField()
    wallet = models.ForeignKey("Wallet",on_delete= models.CASCADE,related_name= "card_wallet", null=True)
    account = models.ForeignKey("Account",on_delete= models.CASCADE, related_name= "card_account", null=True)
    card_status = models.CharField(max_length= 15,null=True)

class ThirdParty(models.Model):
    party_name = models.CharField(max_length= 15,null=True)
    account = models.ForeignKey("Account",on_delete= models.CASCADE, related_name= "ThirdParty_account")
    party_id = models.PositiveSmallIntegerField(null=True)
    phone_number = models.IntegerField()

class Notifications(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length= 15,null=True)
    notification_date_time = models.DateTimeField()
    recipient = models.ForeignKey("Receipt",on_delete= models.CASCADE, related_name= "notification_recipient")
    STATUS = (
        ('R','Read'),
        ('U','Unread')
    )
    notification_status = models.CharField(max_length= 1, choices= STATUS)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length= 8,null=True)
    receipt_date = models.DateTimeField()
    receipt_file = models.FileField(null=True)
    total_amount = models.IntegerField(null=True)
    account_number = models.IntegerField()
    transaction = models.ForeignKey("Transaction",on_delete= models.CASCADE, related_name= "receipt_transaction")

class Loan(models.Model):
    loan_number = models.IntegerField(null=True)
    loan_type = models.CharField(max_length= 15,null=True)
    loan_amount = models.IntegerField(null=True)
    loan_date = models.DateTimeField(null=True)
    wallet = models.ForeignKey("Wallet",on_delete= models.CASCADE, related_name= "loan_wallet")
    interest_rate = models.IntegerField()
    loan_guaranter = models.ForeignKey("Customer", on_delete= models.CASCADE, related_name= "loan_loan", null=True)
    loan_due_date = models.DateTimeField(null=True)
    loan_balance = models.IntegerField()
    loan_term = models.IntegerField(null=True)

class Reward(models.Model):
    transaction = models.ForeignKey("Transaction",on_delete= models.CASCADE, related_name= "reward_transaction")
    reward_date = models.DateTimeField()
    customer_id = models.IntegerField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length= 15,choices= GENDER_CHOICES, null=True)
    reward_points = models.IntegerField(null=True)



