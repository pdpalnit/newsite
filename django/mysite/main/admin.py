from django.contrib import admin
from .models import Tutorial

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
	# Note that this just make changes in the tutorial which can be done by admin.ModelAdmin.
	# If we change the order of the fields then it does reflect on the site. That's it!
	fields = ["tutorial_title",
			  "tutorial_content",
			  "tutorial_published"]

# Note that we can also register without explicitly passing TutorialAdmin because it is default and we register there only by
# using admin.ModelAdmin
admin.site.register(Tutorial, TutorialAdmin)