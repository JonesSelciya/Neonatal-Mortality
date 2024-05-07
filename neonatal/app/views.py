from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout
from .models import *
from django.http import JsonResponse


# Create your views here.



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('first')
        password = request.POST.get('password')
        # Create a new user using Django's built-in User model
        user = Reg.objects.create_user(username=username, password=password)
        user.name = name  # Set the name field
        user.save()
        # Log the user in after signup
        auth_login(request, user)
        return redirect('home')  # Redirect to the home page after successful signup
    return render(request, "registration.html")
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('first')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('home')


# Assuming Height is in meters, and Weight is in kilograms







def home(request):
    return render (request,'foodplan.html')

def food(request):
    food_plan = ""  # Move this line outside the if block

    if request.method == "POST":
        Sugar = float(request.POST.get('Sugar', 0))
        BP = float(request.POST.get('BP', 0))
        Pregnancy = request.POST.get('Pregnancy')
        illness = request.POST.get('illness')
        Weight = int(request.POST.get('Weight'))
        Height = int(request.POST.get('Height'))
        BMI = int(request.POST.get('bmi'))
        

        food_plan = ""  # Initialize food_plan variable

        # Example conditions based on your requirements
        if BMI <= 18:
            food_plan += "Consider a diet for underweight individuals. "
        elif BMI >= 19 and BMI < 25:
            food_plan += "You are in a healthy weight range. "
        else:
            food_plan += "Consider a diet for overweight or obese individuals. "
       
       
       
        if "Consider a diet for underweight individuals" in food_plan:
            return render(request, 'fooddiet1.html')
        if  "You are in a healthy weight range. " in food_plan:
            return render(request, 'fooddiet2.html')
        
        elif "Consider a diet for overweight or obese individuals" in food_plan:
            return render(request, 'fooddiet3.html')

   

    return render(request, 'food.html')

def Appointment(request):
    if request.method=="POST":
        Doctor=request.POST.get('Doctor')
        Date=request.POST.get('Date')
        Patient=request.POST.get('Patient')
        Treatment=request.POST.get('Treatment')
        Contact=request.POST.get('Contact')

       

        appointment = appoint.objects.create(
        Doctor=Doctor,
        Date=Date,
        Patient=Patient,
        Treatment=Treatment,
        Contact=Contact
    )

    # Save the appointment to the database
        appointment.save()
        msg="Appointment Subitted successfully"
        return render(request,'appointment.html', {'msg': msg})

    return render(request,'appointment.html')




def workout(request):
    if request.method == "POST":
        BMI = float(request.POST.get('bmi', 0))
        Sugar = float(request.POST.get('Sugar', 0))
        BP = float(request.POST.get('BP', 0))
        Pregnancy = int(request.POST.get('Pregnancy', 0))

        if 1 <= Pregnancy <= 3:
            return render(request, 'workoutplan1.html')
        elif 4 <= Pregnancy <= 6:
            return render(request, 'workoutplan2.html')
        elif 6 <= Pregnancy <= 9:
            return render(request, 'workoutplan3.html')

    return render(request, 'workout.html')






def vaccination(request):
    return render (request,'vaccination.html')


def Center(request):
    if request.method=="GET":
        value=request.GET.get('city')
        print(value)
        cate=center.objects.filter(city=value)
    return render (request,'vaccination.html',{'form':cate})




def Scheme(request):
    return render (request,'Scheme.html')





def chatbot(request):
    if request.method == "POST":
        try:
            bot = request.POST.get('messageText')
            user_responses = chat.objects.filter(botreply=bot).values_list("response", flat=True)
            
            if user_responses:
                bot_response = str(user_responses[0])
            else:
                # If no matching response is found, provide a default message
                bot_response = "Sorry, I don't understand."

            print(bot_response)
            return JsonResponse({'status': 'OK', 'answer': bot_response})

        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Exception: {e}")
            return JsonResponse({'status': 'Error', 'answer': 'An error occurred'})
    
    return render(request, 'chat.html')


