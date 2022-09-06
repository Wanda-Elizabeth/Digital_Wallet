from django.urls import path 
from .views import register_account, register_card, register_currency, register_loan, register_loans, register_notifications, register_reciept, register_reward, register_third_party, register_transaction, register_wallet, register_customer

urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="registration"),
    path("currency/",register_currency,name="registration"),
    path("account/",register_account,name="registration"),
    path("transaction/",register_transaction,name="registration"),
    path("card/",register_card,name="registration"),
    path("third_party/",register_third_party,name="registration"),
    path("notifications/",register_notifications,name="registration"),
    path("reciept/",register_reciept,name="registration"),
    path("loan/",register_loan,name="registration"),
    path("reward/",register_reward,name="registration"),

]