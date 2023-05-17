from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
# from joblib import load


# Create your views here.
# model = load('./savedModules/module.joblib')
# vectorizer = load('./savedModules/vectorizer.joblib')
# diabetes_model = load('./savedModules/diabetes.joblib')

def main(request):

    all_posts = Post.newmanager.all()
    # if request.method == 'POST':
    #     ip = request.POST['ip']
    #     y_pred = model.predict(vectorizer.transform([ip]))
    #     print(y_pred[0])
    #     return render(request, 'index.html', {'result' : y_pred[0]})
    return render(request, 'index.html', {'posts' : all_posts})
        # return HttpResponse("This is home!!")

def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    return render(request, 'single.html', {'post' : post})


def test(request):
    return render(request,'dia_res.html')

def translated(request):
    return render(request,'translated_single.html')

# def diabetes(request):
#     pregnancy = request.GET['Pregnancy']
#     glucose = request.GET['Glucose']
#     bp = request.GET['BP']
#     st = request.GET['Skin Thickness']
#     insulin = request.GET['Insulin']
#     bmi = request.GET['BMI']
#     dpf = request.GET['DPF']
#     age = request.GET['Age']
#     y_pred_dia = diabetes_model.predict([[pregnancy, glucose, bp, st, insulin, bmi, dpf, age]])
#     if(y_pred_dia[0] == 0):
#         res = "Negative"
#     else:
#         res = "Positive"
#     print(y_pred_dia[0])
#     return render(request, "resdia.html", {'resdia' : res})

def pagedia(request):
    return render(request, "dia_res.html")

# def signup(request):
#     return render(request, "signup.html")

# def signin(request):
#     return render(request, "signin.html")

# def signout(request):
#     pass