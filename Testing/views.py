from django.shortcuts import render
import joblib






# Create your views here.
def testtest(request):
    return render(request,'result.html')
def add(request):
   
   # model=joblib.load(r'C:\Users\ronbr\Desktop\DiabetsProjo\diabetes_predictor.joblib')
    model=joblib.load('model/diabetes_predictor.joblib')

    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val6=float(request.POST['num6'])
    val7=float(request.POST['num7'])
    val8=int(request.POST['num8'])
    
    
    prediction=model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    res=prediction

    if res==0:
        val="Negative"
    else:
        val="Positive"
    
    return render(request,'sample.html',{'result':val})


    