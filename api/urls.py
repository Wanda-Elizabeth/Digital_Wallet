from django.db import router
from django.urls import path,include
from rest_framework import routers
from.views import AccountDepositView, AccountViewsets, CardViewsets, CustomerViewsets, LoanViewsets, NotificationsViewsets, ReceiptViewsets, TransactionViewsets, WalletViewsets

router=routers.DefaultRouter()
router.register("customers",CustomerViewsets)
router.register("wallets",WalletViewsets)
router.register("cards",CardViewsets)
router.register("accounts",AccountViewsets)
router.register("transactions",TransactionViewsets)
router.register("loans",LoanViewsets)
router.register("notification",NotificationsViewsets)
router.register("receipts",ReceiptViewsets)


urlpatterns = [
    path("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),


   


]