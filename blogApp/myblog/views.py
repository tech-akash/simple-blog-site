from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .models import blogModel
from .forms import createBlogForm


# this is list view that shows all the blog on the home page
def home_view(request,*args, **kwargs):
    blogList=blogModel.objects.all()
    print(blogList)
    context={
        'blogList':blogList,
    }
    return render(request,'home.html',context)


# this is view is responsible for creating blogs
def create_view(request,*args, **kwargs):
    '''
    form imported from forms.py main purpose is to handel the content of blog written using
    froala editor
    '''
    form=createBlogForm(request.POST or None)
    if request.method == 'POST':
        # getting file title from request.file and request.post
        image = request.FILES['image']
        title = request.POST.get('title')
        if form.is_valid():
            # if form is valid we grab the content from it
            content=form.cleaned_data.get('blogContent')
            # creating the blog
            obj=blogModel.objects.create(blog_title=title,blogContent=content,blog_image=image)
            return redirect('create')
        

    context={
        'form':form
    }
    return render(request,'createBlog.html',context)

# this is single blog view shows details of blogs
def detail_view(request,pk,*args, **kwargs):
    # grabs the object with passed primary key (pk)
    obj=blogModel.objects.get(id=pk)
    # checks if object is found then pass it to context otherwise raise http404 
    time=obj.timeStamp.time()
    print(time)
    if obj is not None:
        context={"obj":obj}
    else:
        raise Http404("Page Not Found! :(")
    return render(request,"detail.html",context)


def update_view(request,pk,*args, **kwargs):
    # getting object to be updated
    obj=blogModel.objects.get(id=pk)
    
    initval={'blogContent':obj.blogContent}
    # passing intial content to the form
    form=createBlogForm(initial=initval)
    if request.method == 'POST':
        form=createBlogForm(request.POST)
        # checks if user passed image if not it will take inital image
        try:
            image = request.FILES['image']
        except Exception as e :
            image=obj.blog_image
        title = request.POST.get('title')
        if form.is_valid():
            content=form.cleaned_data['blogContent']
            # setting the values to  the object and saving it
            obj.blog_title=title
            obj.blog_image=image
            obj.blogContent=content
            obj.save()
        else:
            print(form.errors)  
    
    context={'obj':obj,'form':form}
    return render(request,'updateblog.html',context)


def delete_view(request,pk,*args, **kwargs):
    # try to delete a object if it is present otherwise raise http404
    try:
        obj=blogModel.objects.get(id=pk)
        obj.delete()
    except Exception as e:
        raise Http404("Blog not Found!")
    # after deleting object it redirects to home page
    return redirect("home")

    

    

    
