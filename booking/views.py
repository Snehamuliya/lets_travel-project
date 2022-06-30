from django.shortcuts import render, redirect
from django.http import HttpResponse
import pymongo
import razorpay


# Create your views here.
key_id = 'rzp_test_9RtNNEpX0ToXnn'
key_secrete = 'lUJVgqij275N2dId2eXpCrkE'
pclient = razorpay.Client(auth=(key_id, key_secrete))


def index(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'index.html', u_session)


def holiday(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'package.html', u_session)


def kerla(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    print("kerla")
    return render(request, 'kerla.html', u_session)


def kerla2(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'kerla 2.html', u_session)


def kerla3(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'kerla3.html', u_session)


def goa2(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'goa2.html', u_session)


def goa1(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'goa1.html', u_session)


def karnatak1(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'karnatak1.html', u_session)


def andman1(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'andman1.html', u_session)


def andman2(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    return render(request, 'andman2.html', u_session)


def cor_trip(request):
    id = 0
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['booking']
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    if request.method == 'GET':
        return render(request, 'co_trip.html', u_session)
    else:
        if 'andman1' in request.POST:
            u_session['trip'] = 'A1 - ANDAMAN'
            u_session['price'] = 30990
            return render(request, 'booking.html', u_session)
        elif 'kerla1' in request.POST:
            u_session['trip'] = 'k1 - MUNNAR PERIYAR ALLEPPY'
            u_session['price'] = 24990
            return render(request, 'booking.html', u_session)
        elif 'goa1' in request.POST:
            u_session['trip'] = 'g1 - GOA - MY FAIR LADY'
            u_session['price'] = 15990
            return render(request, 'booking.html', u_session)
        elif 'book' in request.POST:
            bookc = collection.count_documents({})
            id = bookc + 1
            name = request.POST.get('fname')
            address = request.POST.get('add')
            mobile = request.POST.get('num')
            email = request.POST.get('mail')
            aadhar = request.POST.get('adhar')
            user = request.POST.get('user')
            trips = request.POST.get('trip')
            price = request.POST.get('t_price')
            quest = request.POST.get('ques')
            member = request.POST.get('peo_no')

            final = int(member) * int(price)
            print(name, address, mobile, email, aadhar, user, trips, quest, member, price)
            request.session['billno'] = id
            request.session['total'] = final
            Data = {
                'amount': final * 100,
                'currency': 'INR',
                'notes': {
                    'name': name,
                    'payment_for': trips
                }
            }
            order = pclient.order.create(data=Data)
            print(order)
            print(order.get('id'))
            pid = order.get('id')
            request.session['payid'] = order.get('id')
            dictionary1 = {'b_id': id, 'name': name, 'address': address, 'phone': mobile, 'mail_id': email,
                           'aadhar_no': aadhar, 'username': user, 'trip': trips, 'query': quest, 'no_of_member': member,
                           'trip_price': price, 'amount': final, 'pay_id': pid}
            collection.insert_one(dictionary1)
            return redirect('checkout')


def family_trip(request):
    id = 0
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['booking']
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    if request.method == 'GET':
        return render(request, 'family_trip.html', u_session)
    else:
        if 'andman2' in request.POST:
            u_session['trip'] = 'A2 - ANDAMAN'
            u_session['price'] = 29990
            return render(request, 'booking.html', u_session)
        elif 'kerla2' in request.POST:
            u_session['trip'] = 'k2 - MUNNAR PERIYAR ALLEPPY'
            u_session['price'] = 26990
            return render(request, 'booking.html', u_session)
        elif 'goa2' in request.POST:
            u_session['trip'] = 'g2 - GOA WITH LAKSHADWEEP'
            u_session['price'] = 20000
            return render(request, 'booking.html', u_session)
        elif 'book' in request.POST:
            bookc = collection.count_documents({})
            id = bookc + 1
            name = request.POST.get('fname')
            address = request.POST.get('add')
            mobile = request.POST.get('num')
            email = request.POST.get('mail')
            aadhar = request.POST.get('adhar')
            user = request.POST.get('user')
            trips = request.POST.get('trip')
            price = request.POST.get('t_price')
            quest = request.POST.get('ques')
            member = request.POST.get('peo_no')

            final = int(member) * int(price)
            print(name, address, mobile, email, aadhar, user, trips, quest, member, price)

            request.session['billno'] = id
            request.session['total'] = final
            Data = {
                'amount': final * 100,
                'currency': 'INR',
                'notes': {
                    'name': name,
                    'payment_for': trips
                }
            }
            order = pclient.order.create(data=Data)
            print(order)
            print(order.get('id'))
            pid = order.get('id')
            request.session['payid'] = order.get('id')
            dictionary1 = {'b_id': id, 'name': name, 'address': address, 'phone': mobile, 'mail_id': email,
                           'aadhar_no': aadhar, 'username': user, 'trip': trips, 'query': quest, 'no_of_member': member,
                           'trip_price': price, 'amount': final, 'pay_id': pid}
            collection.insert_one(dictionary1)
            return redirect('checkout')


def little_break(request):
    id = 0
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['booking']
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    if request.method == 'GET':
        return render(request, 'little_break.html', u_session)
    else:
        if 'kar1' in request.POST:
            u_session['trip'] = 'kar1 - HAMPI BADAMI'
            u_session['price'] = 25990
            return render(request, 'booking.html', u_session)
        elif 'kerla3' in request.POST:
            u_session['trip'] = 'k3 - KERALA KANYAKUMARI MADURAI'
            u_session['price'] = 27990
            return render(request, 'booking.html', u_session)
        elif 'book' in request.POST:
            bookc = collection.count_documents({})
            id = bookc + 1
            name = request.POST.get('fname')
            address = request.POST.get('add')
            mobile = request.POST.get('num')
            email = request.POST.get('mail')
            aadhar = request.POST.get('adhar')
            user = request.POST.get('user')
            trips = request.POST.get('trip')
            price = request.POST.get('t_price')
            quest = request.POST.get('ques')
            member = request.POST.get('peo_no')

            final = int(member) * int(price)
            print(name, address, mobile, email, aadhar, user, trips, quest, member, price)

            request.session['billno'] = id
            request.session['total'] = final
            Data = {
                'amount': final * 100,
                'currency': 'INR',
                'notes': {
                    'name': name,
                    'payment_for': trips
                }
            }
            order = pclient.order.create(data=Data)
            print(order)

            pid = order.get('id')
            request.session['payid'] = order.get('id')
            dictionary1 = {'b_id': id, 'name': name, 'address': address, 'phone': mobile, 'mail_id': email,
                           'aadhar_no': aadhar, 'username': user, 'trip': trips, 'query': quest, 'no_of_member': member,
                           'trip_price': price, 'amount': final, 'pay_id': pid}
            collection.insert_one(dictionary1)
            return redirect('checkout')



def payment(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['travel']
    collection = db['booking']
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    u_session['bill_id'] = request.session.get('billno')
    u_session['amount'] = request.session.get('total')
    u_session['payment_id'] = request.session.get('payid')
    if request.method == 'GET':
        one = collection.find_one({'b_id': u_session['bill_id']})
        u_session['b_data'] = one
        return render(request, 'payment.html', u_session)
    else:
        #del request.session['billno']
        return redirect('log')





def profile(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    db = client['travel']
    collection = db['users']
    one = collection.find_one({'username': u_session['s_user']})
    u_session['s_data'] = one

    return render(request, 's_profile.html', u_session)


def useracc_upd(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    db = client['travel']
    collection = db['users']
    if request.method == 'GET':
        one = collection.find_one({'username': u_session['s_user']})
        u_session['s_data'] = one
        return render(request, 'uacc_update.html', u_session)
    else:
        postdata = request.POST
        firstname = postdata.get('fname')
        u_add = postdata.get('add')
        u_no = postdata.get('no')
        u_mail = postdata.get('mail')
        u_aadhar = postdata.get('aadhar')
        u_user = postdata.get('user')
        u_pass = postdata.get('pass')
        origin = {'username': u_session['s_user']}
        ac = collection.count_documents({'username': u_user})
        print(ac)
        upd = {
            '$set': {'name': firstname, 'address': u_add, 'mobile': u_no, 'mail_id': u_mail, 'aadhar_no': u_aadhar,
                     'username': u_user, 'password': u_pass}}
        collection.update_one(origin, upd)
        return redirect('u_profile')





def u_activity(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['booking']
    if request.method == 'GET':
        data = collection.find({'username': u_session['s_user']})
        u_session['s_data'] = data
        return render(request, 's_activity.html', u_session)
    else:
        if 'del' in request.POST:
            postdata = request.POST
            pid = postdata.get('pay')
            # re_id = str(recid)
            collection.delete_one({'pay_id': pid})
            return redirect("act")
        elif 'receipt' in request.POST:
            postdata = request.POST
            recid = postdata.get('rid')
            pid = postdata.get('pay')
            u_session['r_id'] = recid
            one = collection.find_one({'pay_id': pid})
            u_session['r_data'] = one
            return render(request, 'receipt.html', u_session)







def receipt(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    u_session['rec_id'] = request.session.get('r_id')
    if request.method == 'GET':
        return render(request, 'receipt.html', u_session)
    else:
        #del request.session['billno']
        return redirect('log')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print(client)
        db = client['travel']
        collection = db['users']
        postdata = request.POST
        firstname = postdata.get('fname')
        address = postdata.get('add')
        phone = postdata.get('num')
        email = postdata.get('mail')
        aadhar = postdata.get('adhar')
        userid = postdata.get('user')
        passw = postdata.get('pass')
        ac = collection.count_documents({'username': userid})
        print(ac)
        if ac == 0:
            dictionary1 = {'name': firstname, 'address': address, 'mobile': phone, 'mail_id': email, 'aadhar_no': aadhar, 'username': userid, 'password': passw}
            collection.insert_one(dictionary1)
            return render(request, 'signup.html')
        else:
            data = {}
            data['msg'] = "user allready exist"
            return render(request, 'signup.html',data)


def book(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['travel']
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    if request.method == 'GET':
        print("get book")
        return render(request, 'booking.html', u_session)
    else:
        print("post book")
        postdata = request.POST
        user_n = postdata.get('fname')
        password = postdata.get('add')
        print(user_n, password)
        return redirect('f_member')


def member(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    if request.method == 'GET':
        return render(request, 'people.html', u_session)


def user_data(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['users']
    data = collection.find({})
    users = {
        "user_number": data
    }
    return render(request, 'admin/user_data.html', users)


def login(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['travel']
    collection = db['users']
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        postdata = request.POST
        user_n = postdata.get('user')
        password = postdata.get('pass')
        ac = collection.count_documents({'password': password, 'username': user_n})
        print(ac)
        if user_n == "admin" and password == "admin123":
            return redirect('u_data')
        elif ac == 0:
            return HttpResponse("user not found")
        else:
            request.session['user'] = user_n
            u_session = {}
            u_session['s_user'] = request.session.get('user')

            return render(request, 'index.html', u_session)


def feedback(request):
    u_session = {}
    u_session['s_user'] = request.session.get('user')
    if request.method == 'GET':
        return render(request, 'feedback.html', u_session)
    else:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['travel']
        collection = db['feedback']
        postdata = request.POST
        firstname = postdata.get('name')
        email = postdata.get('mail')
        u_query = postdata.get('feed')
        feedc = collection.count_documents({})
        id = feedc + 1
        cid = str(id)
        ac = collection.count_documents({'f_id': cid})
        print(ac)
        if ac == 0:
            fid= str(id)
            dictionary2 = {'f_id': fid, 'name': firstname, 'mail_id': email, 'query': u_query}
            collection.insert_one(dictionary2)
            return render(request, 'feedback.html', u_session) 
        else:
            id = feedc + 2
            fid = str(id)
            ad = collection.count_documents({'f_id': fid})
            if ad == 0:
                
                dictionary2 = {'f_id': fid, 'name': firstname, 'mail_id': email, 'query': u_query}
                collection.insert_one(dictionary2)
                return render(request, 'feedback.html', u_session) 
            else:
                id = feedc + 10
                fid = str(id)
                dictionary2 = {'f_id': fid, 'name': firstname, 'mail_id': email, 'query': u_query}
                collection.insert_one(dictionary2)
                return render(request, 'feedback.html', u_session)
            
             
              
        


def logout(request):
    del request.session['user']
    return redirect('log')



def a_login(request):
    data = {}
    if request.method == "GET":
        return render(request, 'a_login.html')
    else:
        if 'log' in request.POST:
            name = request.POST.get('user')
            passw = request.POST.get('pass')
            if name == 'admin' and passw == 'admin123':
                request.session['a_user'] = name
                data['ad_user'] = request.session.get('a_user')
                print(request.session['a_user'])
                return render(request, 'admin/a_home.html', data)
            else:
                data['msg'] = 'enter valid username or password'
                return render(request, 'a_login.html', data)


def logout(request):
    del request.session['a_user']
    return redirect('adlog')


def ahome(request):
    data= {}
    data['ad_user'] = request.session.get('a_user')
    return render(request, 'admin/a_home.html', data)



def user_feedback(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['feedback']
    if request.method == "GET":
        fdata = collection.find({})
        data['feed_data'] = fdata
        return render(request, 'admin/a_feed.html', data)
    else:
        if 'feed' in request.POST:
            fid = request.POST.get('fe_id')
            collection.delete_one({'f_id': fid})

            return redirect('feed')
            
    
def user_profile(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['users']
    if request.method == "GET":
        adata = collection.find({})
        data['user_data'] = adata
        return render(request, 'admin/a_user.html', data)
    else:
        if 'user' in request.POST:
            uid = request.POST.get('userdata')
            print(uid)
            collection.delete_one({'username': uid})
            return redirect('user')
    
    
def user_booking(request):
    data = {}
    data['ad_user'] = request.session.get('a_user')
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['travel']
    collection = db['booking']
    if request.method == "GET":
        bdata = collection.find({})
        data['book_data'] = bdata
        return render(request, 'admin/a_book.html', data)
    else:
        if 'book' in request.POST:
            bid = request.POST.get('bookdata')
            collection.delete_one({'pay_id': bid})
            return redirect('book')
