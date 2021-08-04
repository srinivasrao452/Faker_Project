
#  pip install faker

from django.shortcuts import render,redirect
from Faker_App.models import Employee

from faker  import  Faker
fake = Faker()

def create_fake_data(request):
    for i  in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.random_element(elements=("Srinivas","Virat","Rohit","Vishnu"))
        email = fake.email()
        salary = fake.random_element(elements=(10000,20000,30000,40000))
        role = fake.random_element(elements=("SE","TL","MGR","PM"))
        mobile = fake.random_int(min=9000, max=999999)
        city = fake.city()

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            salary=salary,
            role=role,
            mobile=mobile,
            city=city
        )
        # emp = Employee(first_name=first_name,)
        # emp.save()

    return redirect('/display_fake_data/')


def display_fake_data(request):
    employee_list = Employee.objects.all() # [{ },{ },{ },...] or [ ]
    manager_role_count = Employee.objects.filter(role='MGR').count()
    salaries = Employee.objects.filter(salary__gte=40000).count()
    context = {
        'employee_list' : employee_list,
        'manager_role_count' : manager_role_count,
        'salaries' : salaries
    }
    return render(request,'display_fake_data.html', context)





