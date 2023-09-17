from django.shortcuts import render,redirect
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def page1(request):
    region={"Scarcity":["Himachal Pradesh","Haryana","Punjab","Uttar Pradesh","Uttarakhand","Chandigarh","Delhi","Jammu and Kashmir","Ladakh","Rajasthan","Gujarat","Dadra and Nagar Haveli and Daman and Diu","Madhya Pradesh","Jharkhand","Bihar","West Bengal",],
    "Stress":["Telangana","Puducherry","Odisha","Karnataka","Chhattisgarh","Maharashtra"],"No Stress":["Meghalaya","Assam","Arunachal Pradesh","Nagaland","Sikkim","Manipur","Mizoram","Tripura","Goa","Kerala"],"Danger":["Andhra Pradesh","Tamil Nadu"]}
    
   
    if request.method=="POST":
        st=request.POST['state']
        shower=int(request.POST['showerTime'])
        flush=int(request.POST['flushes'])
        dish=int(request.POST['dishwasherUsage'])
        laun=int(request.POST['laundryUsage'])
        diet=int(request.POST['dietPlan'])
        
        showertime=9*shower
        flushtime=4.8*flush
        launtime=45*laun
        dishtime=9.5*dish
        totalwater=showertime+flushtime+launtime+dishtime+diet
        pyrwater=totalwater*365


        for k,v in region.items():
            if(st in v ):
                if(k=="Scarcity"):
                    if(pyrwater>500000 and pyrwater<1000000):
                        messages.info(request,'You have good waterfootprint')
                    if(pyrwater<500000):
                        messages.info(request,'You have good waterfootprint, Keep it up')
                    if( pyrwater>1000000):
                        messages.info(request,'You should follow water conservation techniques')
                if(k=="Stress"):
                    if(pyrwater>1000000 and pyrwater<1700000):
                        messages.info(request,'You have good waterfootprint')
                    if(pyrwater<1000000):
                        messages.info(request,'You have good waterfootprint, Keep it up')
                    if( pyrwater>1700000):
                        messages.info(request,'You should follow water conservation techniques')
                if(k=="No Stress"):
                    if(pyrwater<1700000):
                        messages.info(request,'You have good waterfootprint')
                    if( pyrwater>1700000):
                        messages.info(request,'You have good waterfootprint, Keep it up')
                if(k=="Danger"):
                    if(pyrwater<500000):
                        messages.info(request,'You have good waterfootprint,Keep it up')
                    if( pyrwater>500000):
                        messages.info(request,'You should follow water conservation techniques')
        return render(request,'result.html',{'totalwater':totalwater})
    else:
        return render(request,'page1.html')
    
def resultpage(request):
    return render(request,'result.html')
def aboutus(request):
    return render(request,'aboutus.html')
def divconnect1(request):
    return render(request,'divconnect1.html')
def divconnect2(request):
    return render(request,'divconnect2.html')
def divconnect3(request):
    return render(request,'divconnect3.html')






# Create your views here.
