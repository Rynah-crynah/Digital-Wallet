# from unicodedata import name
from django.urls import path
from .views import account_details, card_details, customer_reward, loan_details, notify_customer, recieve_reciept, register_customer, third_party_details, transaction_details, wallet_information

urlpatterns = [
    path("register/",register_customer, name ="registration"),
    path("wallet/",wallet_information, name = "wallet"),
    path("account/",account_details, name= "account"),
    path("transaction/",transaction_details, name= "transaction"),
    path("card/",card_details, name= "card"),
    path("thirdparty/",third_party_details, name= "thidparty"),
    path("notify/",notify_customer, name= "notifications"),
    path("reciept/",recieve_reciept, name= "reciept"),
    path("loan/",loan_details, name= "loan"),
    path("reward/",customer_reward, name= "reward"),
]