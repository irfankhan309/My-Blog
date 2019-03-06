from django.shortcuts import render
# from irfanApp.models import files_tab
# Create your views here.

class My_views:
    def index(request):
        return render(request,'irfanApp/index.html')
    #
    # def file_view(request):
    #     file_loaded=files_tab.objects.all()
    #     return render(request,'irfanApp/index.html',{'file_loaded':file_loaded})
