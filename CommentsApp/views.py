from django.shortcuts import render

# Create your views here.
from . import models
from . import forms

#from . import forms
# Create your views here.
def getComments(request):
    comments_list = models.Comment.objects.all()
    context = {
        'comments' : comments_list,
    }
    return render(request, 'comments.html', context)

def getCommentForm(request):
    return render(request, 'ommentForm.html')

def addComment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'])
            new_comment.save()
            comments_list = models.Comment.objects.all()
            context = {
                'comments' : comments_list,
            }
            return render(request, 'comments.html', context)
        else:
            form = forms.CommentForm()
    return render(request, 'comments.html')
