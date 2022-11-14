from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet
from .serializer import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, NotificationsSerializer, ReceiptSerializer, TransactionSerializer, WalletSerializer
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist



class CustomerViewsets(viewsets.ModelViewSet):

    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class WalletViewsets(viewsets.ModelViewSet):

    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer

class AccountViewsets(viewsets.ModelViewSet):

    queryset=Account.objects.all()
    serializer_class=AccountSerializer

class AccountDepositView(views.APIView):
  
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)

class CardViewsets(viewsets.ModelViewSet):

    queryset=Card.objects.all()
    serializer_class=CardSerializer

class TransactionViewsets(viewsets.ModelViewSet):

    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

class LoanViewsets(viewsets.ModelViewSet):

    queryset=Loan.objects.all()
    serializer_class=LoanSerializer

class ReceiptViewsets(viewsets.ModelViewSet):

    queryset=Receipt.objects.all()
    serializer_class=ReceiptSerializer    

class NotificationsViewsets(viewsets.ModelViewSet):

    queryset=Notifications.objects.all()
    serializer_class=NotificationsSerializer    

 