from django.shortcuts  import render
from joblib import load

model = load('./models/model.joblib')

# Create your views here.

def Welcome(request):
    return render( request,'index.html')

def formInfo(request):
    filepath = request.POST['filePath']
    upload_img = model.predict([filepath])
    print(upload_img)
    return render(request,'result.html')