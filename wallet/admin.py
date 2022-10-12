import email
from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, Third_Party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email")
    search_fields=("fast_name","lastname","email")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("balance","customer_id","time","status")
    search_fields=("balance","customer_id","time","status")
admin.site.register(Wallet,WalletAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("country","symbol")
    search_fields=("currency","symbol")
admin.site.register(Currency,CurrencyAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_number","account_type","balance")
    search_fields=("account_number","account_type",)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_code","transaction_amount","wallet","transaction_charge")
    search_fields=("transaction_code","transaction_amount","wallet","transaction_charge")
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("issue_date","card_name","card_number")
    search_fields=("issue_date","card_name","card_number")
admin.site.register(Card,CardAdmin)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=("name","id","type","transaction_account","account","currency")
    search_fields=("name","id","type","transaction_account","account","currency")
admin.site.register(Third_Party,Third_partyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display=("transaction","transaction_id","transaction_amount","customer_id")
    search_fields=("transaction","transaction_id","transaction_amount","customer_id")
admin.site.register(Notifications,NotificationsAdmin)

class RecieptAdmin(admin.ModelAdmin):
    list_display=("receipt_type","receipt_date","bill_number","total_amount","transaction","receipt_file")
    search_fields=("receipt_type","receipt_date","bill_number","total_amount","transaction","receipt_file")
admin.site.register(Receipt,RecieptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_id","loan_type","amount","datetime","wallet","intrest_rate")
    search_fields=("loan_id","loan_type","amount","datetime","wallet","intrest_rate")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("name","customer_id","gender","points","date_of_reward","recipient")
    search_fields=("name","customer_id","gender","points","date_of_reward","recipient")
admin.site.register(Reward,RewardAdmin)




    
    

