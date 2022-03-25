from django.shortcuts import render
from fitnessclub.models import AllImages, MoreImages, MyImages
from fitnessclub import forms

def homePage(request):
    images = AllImages.objects.get(imageInformation="logo").image 
    homePageImage = AllImages.objects.get(imageInformation="homepageImage").image
    aboutImage = AllImages.objects.get(imageInformation="aboutImage").image
    form = forms.EmailSendForm()
    image1 = MoreImages.objects.get(title="Image1").image
    image2 = MoreImages.objects.get(title="Image2").image
    image3 = MoreImages.objects.get(title="Image3").image
    image4 = MoreImages.objects.get(title="Image4").image
    image5 = MoreImages.objects.get(title="Image5").image
    image6 = MoreImages.objects.get(title="Image6").image
    image7 = MoreImages.objects.get(title="Image7").image
    image8 = MoreImages.objects.get(title="Image8").image
    image9 = MoreImages.objects.get(title="Image9").image
    image10 = MoreImages.objects.get(title="Image10").image
    image11 = MoreImages.objects.get(title="Image11").image
    image12 = MoreImages.objects.get(title="Image12").image
    image13 = MoreImages.objects.get(title="Image13").image
    image14 = MoreImages.objects.get(title="Image14").image

    pic1 = MyImages.objects.get(title="Image2").image
    pic2 = MyImages.objects.get(title="Image4").image
    pic3 = MyImages.objects.get(title="Image5").image
    pic4 = MyImages.objects.get(title="Image6").image
    pic5 = MyImages.objects.get(title="Image30").image
    pic6 = MyImages.objects.get(title="Image8").image
    pic7 = MyImages.objects.get(title="Image10").image
    pic8 = MyImages.objects.get(title="Image12").image
    pic9 = MyImages.objects.get(title="Image19").image
    pic10 = MyImages.objects.get(title="Image20").image
    pic11 = MyImages.objects.get(title="Image22").image
    pic12 = MyImages.objects.get(title="Image23").image
    pic13 = MyImages.objects.get(title="Image24").image
    pic14 = MyImages.objects.get(title="Image25").image
    pic15 = MyImages.objects.get(title="Image26").image
    pic16 = MyImages.objects.get(title="Image33").image
    pic17 = MyImages.objects.get(title="Image34").image
    pic18 = MyImages.objects.get(title="Image15").image
    pic61 = MyImages.objects.get(title="Image61").image
    pic62 = MyImages.objects.get(title="Image62").image

    return render(request,'fitnessclub/home.html',
    {
        'image':images,
        'homePage':homePageImage,
        'about':aboutImage,
        'form':form,
        'image1':image1,
        'image2':image2,
        'image3':image3,
        'image4':image4,
        'image5':image5,
        'image6':image6,
        'image7':image7,
        'image8':image8,
        'image9':image9,
        'image10':image10,
        'image12':image12,
        'image13':image13,
        'image14':image14,
        'image11':image11,
        'pic1' : pic1,
        'pic2' : pic2,
        'pic3' : pic3,
        'pic4' : pic4,
        'pic5' : pic5,
        'pic6' : pic6,
        'pic7' : pic7,
        'pic8' : pic8,
        'pic9' : pic9,
        'pic10' : pic10,
        'pic11' : pic11,
        'pic12' : pic12,
        'pic13' : pic13,
        'pic14' : pic14,
        'pic15' : pic15,
        'pic16' : pic16,
        'pic17' : pic17,
        'pic18' : pic18,
        'pic61' : pic61,
        'pic62' : pic62,
        })
    