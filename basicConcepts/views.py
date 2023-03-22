from django.shortcuts  import render
from .forms import ImageUploadForm
# from joblib import load

# model = load('./models/model.joblib')

# Create your views here.

def Welcome(request):
    return render( request,'index.html')

# def formInfo(request):
#     filepath = request.POST['filePath']
#     upload_img = model.predict([filepath])
#     print(upload_img)
#     return render(request,'result.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Do something with the uploaded image
            image = form.cleaned_data['image']

            print(image)
            # ...
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
