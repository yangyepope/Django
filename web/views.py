from django.shortcuts import render

# Create your views here.


from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    # return HttpResponse("登录页面")
    # return redirect("https://www.baidu.com")
    return render(request, "login.html")


def user_list(request):
    data_list = ["吴佩琪", "李立权", "章程"]
    mapping = {"name": "wupeiqi", "age": 21, "gender": "男"}
    # 打开文件并读取内容
    # 模板的渲染 -》 文本替换
    return render(request, "user_list.html", {"message": "标题来了", "data_list": data_list, "information": mapping})


def phone_list(request):
    queryset = [
        {"id": 1, "phone": "18890909090", "city": "上海"},
        {"id": 2, "phone": "18890909091", "city": "北京"},
        {"id": 3, "phone": "18890909092", "city": "武汉"},
        {"id": 4, "phone": "18890909093", "city": "成都"}
    ]

    return render(request,"phone_list.html",{"data":queryset})
