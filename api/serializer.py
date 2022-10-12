from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Customer
        fields=('first_name','last_name','email')

class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model=Wallet
        fields=("balance","customer_id","time","status")  

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model=Account
        fields=("account_number","account_type","balance")

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model=Card
        fields=("issue_date","card_name","card_number")


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Transaction
        fields=("transaction_code","transaction_amount","wallet","transaction_charge")

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model=Loan
        fields=("loan_id","loan_type","amount","datetime","wallet","intrest_rate")

class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model=Receipt
        fields=("receipt_type","receipt_date","bill_number","total_amount","transaction","receipt_file")

class NotificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Notifications
        fields=("transaction","transaction_id","transaction_amount","customer_id")       






        