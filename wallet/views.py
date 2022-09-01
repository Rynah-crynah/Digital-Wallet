from django.shortcuts import render

from wallet.forms import CustomerRegistrationForm

# Create your views here.

# NOTE: what is contained inside http request?
# 

def register_customer(request):
    from .forms import CustomerRegistrationForm
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})


from django.shortcuts import render
# Create your views here.



def wallet_information(request):
    from .forms import WalletInformation
    form = WalletInformation()
    return render(request,"wallet/wallet_information.html",{"form":form})

def account_details(request):
    from .forms import AccountDetails
    form = AccountDetails()
    return render(request,"wallet/account_details.html",{"form":form})

def transaction_details(request):
    from .forms import TransactionDetails
    form = TransactionDetails()
    return render(request,"wallet/transaction_details.html",{"form":form})

def card_details(request):
    from .forms import CustomerCardDetails
    form = CustomerCardDetails()
    return render(request,"wallet/card_details.html",{"form":form})

def third_party_details(request):
    from .forms import ThirdPartyDetails
    form = ThirdPartyDetails()
    return render(request,"wallet/third_party_details.html",{"form":form})

def notify_customer(request):
    from .forms import CustomerNotifications
    form = CustomerNotifications()
    return render(request,"wallet/notify_customer.html",{"form":form})

def recieve_reciept(request):
    from .forms import TransactionReciept
    form = TransactionReciept()
    return render(request,"wallet/recieve_reciept.html",{"form":form})

def loan_details(request):
    from .forms import LoanDetails
    form = LoanDetails()
    return render(request,"wallet/loan_details.html",{"form":form})

def customer_reward(request):
    from .forms import CustomerReward
    form = CustomerReward()
    return render(request,"wallet/customer_reward.html",{"form":form})


    
    
  

