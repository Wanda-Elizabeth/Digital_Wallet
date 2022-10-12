from django.urls import path 
from .views import account_profile, card_profile, currency_profile, customer_profile, edit_profile, list_account, list_card, list_currency, list_customers, list_loan, list_notifications, list_reciept, list_reward, list_third_party, list_transaction, list_wallet, loan_profile, notifications_profile, reciept_profile, register_account, register_card, register_currency, register_loan, register_notifications, register_reciept, register_reward, register_third_party, register_transaction, register_wallet,register_customer, reward_profile, third_party_profile, transaction_profile, wallet_profile

urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="registration"),
    path("currency/",register_currency,name="registration"),
    path("account/",register_account,name="registration"),
    path("transaction/",register_transaction,name="registration"),
    path("card/",register_card,name="registration"),
    path("third_partys/",register_third_party,name="registration"),
    path("notifications/",register_notifications,name="registration"),
    path("reciept/",register_reciept,name="registration"),
    path("loan/",register_loan,name="registration"),
    path("reward/",register_reward,name="registration"),


    path("customers",list_customers,name="list_customers"),
    path("currency's",list_currency,name="list_currency"),
    path("wallets",list_wallet,name="list_wallet"),
    path("accounts",list_account,name="list_account"),
    path("transactions",list_transaction,name="list_transaction"),
    path("cards",list_card,name="list_card"),
    path("third_parties",list_third_party,name="list_third_party"),
    path("notification",list_notifications,name="list_notifications"),
    path("reciepts",list_reciept,name="list_reciept"),
    path("loans",list_loan,name="list_loan"),
    path("rewards",list_reward,name="list_reward"),


    
    path("customer's/<int:id>/",customer_profile, name="customer_profile"),
    path("wallets/<int:id>/",wallet_profile, name="wallet_profile"),
    path("currency's/<int:id>/",currency_profile, name="currency_profile"),
    path("accounts/<int:id>/",account_profile, name="account_profile"),
    path("transactions/<int:id>/",transaction_profile, name="transaction_profile"),
    path("cards/<int:id>/",card_profile, name="card_profile"),
    path("third_partys/<int:id>/",third_party_profile, name="third_party_profile"),
    path("notification/<int:id>/",notifications_profile, name="notifications_profile"),
    path("reciepts/<int:id>/",reciept_profile, name="reciept_profile"),
    path("loans/<int:id>/",loan_profile, name="loan_profile"),
    path("rewards/<int:id>/",reward_profile, name="reward_profile"),






    path("customer/edit/<int:id>/",edit_profile, name="edit_profile"),
]
