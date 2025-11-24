from newspaper.models import Category
from newspaper.models import Tag
def navigation(request):
    categories = Category.objects.all()
    return {"categories": categories}

def tag_navigation(request):
    tags = Tag.objects.all()
    return {"tags": tags}
