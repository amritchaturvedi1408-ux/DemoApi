from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("This is Home Page")
    friends = [
        "Alok", "Rahul", "Rohit", "Saurabh", "Ankit", "Amit", "Rakesh", "Ramesh", "Suresh"
    ]
    return JsonResponse(friends,safe=False)