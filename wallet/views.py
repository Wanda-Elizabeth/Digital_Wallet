from django.shortcuts import redirect, render

from wallet.models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, Third_Party, Transaction, Wallet

from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, RecieptRegistrationForm, RewardRegistrationForm, Third_PartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

def register_customer(request):
    if request.method=="POST":
         form=CustomerRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",
    {'form':form})

def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/list_customer.html",
    {"customers":customers})


def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request, "wallet/customer_profile.html",{"customer":customer})


    
def edit_customer(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
         form=CustomerRegistrationForm(request.POST,instance=customer)
         if form.is_valid():
            form.save()
         return redirect("customer_profile",id=Customer.id)
    else:
        form=CustomerRegistrationForm()
    return render (request,"wallet/edit_customer.html",
    {'form':form})

def register_currency(request):
    if request.method=="POST":
         form=CurrencyRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=CurrencyRegistrationForm()
    return render (request,"wallet/register_currency.html",
    {'form':form})

def list_currency(request):
    currency=Currency.objects.all()
    return render(request,"wallet/list_currency.html",
    {"currency":currency})   


def register_wallet(request):
    if request.method=="POST":
         form=WalletRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render (request,"wallet/register_wallet.html",
    {'form':form})

def list_wallet(request):
    wallet=Wallet.objects.all()
    return render(request,"wallet/list_wallet.html",
    {"wallet":wallet})   


def register_account(request):
    if request.method=="POST":
         form=AccountRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render (request,"wallet/register_account.html",
    {'form':form})

def list_account(request):
    accounts=Account.objects.all()
    return render(request,"wallet/list_account.html",
    {"accounts":accounts}) 

def register_transaction(request):
    if request.method=="POST":
         form=TransactionRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm()
    return render (request,"wallet/register_transaction.html",
    {'form':form})

def list_transaction(request):
    transaction=Transaction.objects.all()
    return render(request,"wallet/list_transaction.html",
    {"transaction":transaction}) 

def register_notifications(request):
    if request.method=="POST":
         form=NotificationsRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=NotificationsRegistrationForm()
    return render (request,"wallet/register_notifications.html",
    {'form':form})

def list_notifications(request):
    notifications=Notifications.objects.all()
    return render(request,"wallet/list_notifications.html",
    {"notifications":notifications}) 

def register_card(request):
    if request.method=="POST":
         form=CardRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()
    return render (request,"wallet/register_card.html",
    {'form':form})

def list_card(request):
    card=Card.objects.all()
    return render(request,"wallet/list_card.html",
    {"card":card}) 

def register_third_party(request):
    if request.method=="POST":
         form=Third_PartyRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=Third_PartyRegistrationForm()
    return render (request,"wallet/register_third_party.html",
    {'form':form})

def list_third_party(request):
    third_party=Third_Party.objects.all()
    return render(request,"wallet/list_third_party.html",
    {"third_party":third_party}) 
    

def register_reciept(request):
    if request.method=="POST":
         form=RecieptRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=RecieptRegistrationForm()
    return render (request,"wallet/register_reciept.html",
    {'form':form})

def list_reciept(request):
    reciept=Receipt.objects.all()
    return render(request,"wallet/list_reciept.html",
    {"reciept":reciept}) 

def register_loan(request):
    if request.method=="POST":
         form=LoanRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm()
    return render (request,"wallet/register_loan.html",
    {'form':form})

def list_loan(request):
    loan=Loan.objects.all()
    return render(request,"wallet/list_loan.html",
    {"loan":loan}) 

def register_reward(request):
    if request.method=="POST":
         form=RewardRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm()
    return render (request,"wallet/register_reward.html",
    {'form':form})

def list_reward(request):
    reward=Reward.objects.all()
    return render(request,"wallet/list_reward.html",
    {"reward":reward})  
 







