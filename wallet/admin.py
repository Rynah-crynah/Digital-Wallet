from django.contrib import admin
from .models import Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
 list_display = ('first-name', 'last-name', 'age', 'email',)
 search_fields = ('first-name', 'last-name',)
admin.site.register(Customer)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)




