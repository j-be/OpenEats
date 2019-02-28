import json

from django.http import HttpResponse
from models import Ingredient


def autocomplete_ing(request):
    """Used to auto complete ingredient names on the recipe form. This view is called by a jquery script
       returns json list of ten ingredients found
    """
    
    q = request.GET.get('term', '')
    ing_list = Ingredient.objects.filter(title__istartswith=q).values_list('title').distinct().order_by('title')[:10]
    results = []
    for ing_item in ing_list:
        results.append(" ".join(ing_item))
    jsonStr = json.dumps(results)
    return HttpResponse(jsonStr, mimetype="application/json")