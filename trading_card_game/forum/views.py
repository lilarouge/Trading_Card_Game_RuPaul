from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
# Create your views here.
 
def home(request):
    discussions=Discussion.objects.all()
    count=discussions.count()
 
    context={
              'count':count,
              'discussions':discussions
              }
    return render(request,'home.html',context)
 
def addADiscussion(request):
    form = CreateADiscussion()
    if request.method == 'POST':
        form = CreateADiscussion(request.POST)
        if form.is_valid():
# Adding the profile inside the add discussion
            discussion= form.save(commit=False)
            discussion.profile=request.user.profile
            discussion.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'forum/addInForum.html',context)
 
def addAComment(request,pk):
    discussion= Discussion.objects.get(id=pk)
    form = CreateInComment()
    if request.method == 'POST':
        form = CreateInComment(request.POST)
        if form.is_valid():
# adding the profile inside the add comment           
# adding the discussion on the comment
            comment= form.save(commit=False)
            comment.discussion= discussion
            comment.profile=request.user.profile
            comment.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'forum/addInDiscussion.html',context)


def single_discussion(request, discussion_id):
    discussion = Discussion.objects.get(id=discussion_id)
    discussion.profile= request.user.profile 
    
    context= {'discussion': discussion,
                'profile':discussion.profile, 
                }
    return render(request, 'forum/single_discussion.html', context)