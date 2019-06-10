from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
from api_server.models import Account, SysAdmin, Parent, EduOrg, Teacher

MESSAGE_LOGIN_NO_USER_NAME = 'no such username'
MESSAGE_LOGIN_WRONG_PASSWORD = 'wrong password'
MESSAGE_LOGIN_SUCCESS = 'success'

MESSAGE_REGISTER_SUCCESS = 'success'
MESSAGE_REGISTER_ERROR = 'error'


# GET
# login/?username=[username]&password=[password]
def user_login(request):
    ret = {}
    username = request.GET.get('username')
    password = request.GET.get('password')
    obj = Account.objects.filter(user_name=username)
    if len(obj) == 0:
        ret['message'] = MESSAGE_LOGIN_NO_USER_NAME
        return JsonResponse(ret)
    if obj[0].password == password:
        ret['message'] = MESSAGE_LOGIN_SUCCESS
        return JsonResponse(ret)
    else:
        ret['message'] = MESSAGE_LOGIN_WRONG_PASSWORD
        return JsonResponse(ret)


# POST
def user_register(request):
    ret = {}
    try:
        req_json = request.body
        acc = Account()
        acc.user_name = req_json['user_name']
        acc.password = req_json['password']
        acc.email = req_json['email']
        acc.tel = req_json['tel']
        acc.user_type = req_json['user_type']
        acc.save()

        if acc.user_type == 'Parent':
            par = Parent()
            par.user_name = acc.user_name
            par.child_birthday = req_json['child_birthday']
            par.child_gender = req_json['child_gender']
            par.child_name = req_json['child_name']
            par.course_cost = req_json['course_cost']
            par.course_field = req_json['course_field']
            par.course_place = req_json['course_place']
            par.parent_contact = req_json['parent_contact']
            par.parent_name = req_json['parent_name']
            par.save()
        elif acc.user_type == 'EduOrg':
            org = EduOrg()
            org.user_name = acc.user_name
            org.edu_age = req_json['edu_age']
            org.edu_field = req_json['edu_field']
            org.org_address = req_json['org_address']
            org.org_code = req_json['org_code']
            org.org_contact = req_json['org_contact']
            org.org_introduction = req_json['org_introduction']
            org.qualified = req_json['qualified']
            org.save()
        elif acc.user_type == 'Teacher':
            tea = Teacher()
            tea.user_name = acc.user_name
            tea.edu_field = req_json['edu_field']
            tea.edu_age = req_json['edu_age']
            tea.edu_year = req_json['edu_year']
            tea.tea_birthday = req_json['tea_birthday']
            tea.tea_contact = req_json['tea_contact']
            tea.tea_gender = req_json['tea_gender']
            tea.tea_id_number = req_json['tea_id_number']
            tea.tea_introduction = req_json['tea_introduction']
            tea.tea_name = req_json['tea_name']
            tea.qualified = req_json['qualified']
            tea.save()
        else:
            raise BaseException()
    except BaseException as exp:
        ret['message'] = MESSAGE_REGISTER_ERROR
        return JsonResponse(ret)
    ret['message'] = MESSAGE_REGISTER_SUCCESS
    return JsonResponse(ret)


