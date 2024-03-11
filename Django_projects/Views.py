
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

monthly_challanges = {
    "January" : "New Year, New Start!" ,
    "February" : " Walk atleast 20 mins per day!"  ,
    "March" : " Learn Django atleast 20 mins a day!",
    "April" : " Drink eight glass of water daily !",
    "May": " May this month bring the joy!" ,
    "June" : " Exercise atleast 30 mins a day!" ,
    "July" : " Read books regurlarly!" ,
    "August":" Wake up early!" ,
    "September":" Not to skip the  breakfast!" ,
    "October" : " Enjoy the month of october!" ,
    "November": " Eat healty foods!" ,
    "December" : " Save lot of memories!"
}
def index(request):
    list_items = ""
    months = list(monthly_challanges.keys()) 
    for month in months:
        capitalized_month = month.capitalize() 
        month_path = reverse("monthly-challenge",args=[month]) 
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data= f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def  monthly_challange_by_number(request,month):
    months = list(monthly_challanges.keys()) 
    if month > len(months):
        return HttpResponseNotFound("This month did not exist")
    Redirect_response = months[month-1] 
                    # reverse(My_application/January(any month))
    Redirect_path = reverse("monthly-challenge", args=[Redirect_response])
    return HttpResponseRedirect(Redirect_path)


def monthly_challange(request,month):
    try:
        challange_text= monthly_challanges[month] 
        wraped_text = f"<h1>{challange_text}</h1>"
        return HttpResponse(wraped_text)
    except:
        return HttpResponseNotFound("<h1>This month is not supportted!</h1>")    

