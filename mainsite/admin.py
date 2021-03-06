from django.contrib import admin
from mainsite.models import Post, AccessInfo, PlayList, Video, Branch, StoreIncome, Data

class PostAdmin(admin.ModelAdmin):
   list_display = ('title','slug','pub_date')
admin.site.register(PlayList)

class VideoAdmin(admin.ModelAdmin):
   list_display = ('title', 'vid', 'plist')
admin.site.register(Video, VideoAdmin)

class PostAdmin(admin.ModelAdmin):
   list_display = ('title','slug','pub_date')
admin.site.register(Post,PostAdmin)
admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
   list_display = ('title','name')
admin.site.register(Branch,BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
   list_display = ('branch','income_year','income_month','income')
admin.site.register(StoreIncome,StoreIncomeAdmin)

class DataAdmin(admin.ModelAdmin):
   list_display = ('title','name')
admin.site.register(Data,DataAdmin)