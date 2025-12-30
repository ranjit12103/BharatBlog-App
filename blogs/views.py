from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    #Fetch the posts that belongs to the category with the id category_id 
    posts = Blog.objects.filter(status='Published', category = category_id)
    
    
    # try/except when we want custome action if the category does not exists
    # try:
    #     category = Category.objects.get(pk = category_id)
    # except:
    #     return redirect('404')
    
    #Use get_object_or_404 when you want to show 404 page if the category dose not exists
    category = get_object_or_404(Category, pk = category_id)
    
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)