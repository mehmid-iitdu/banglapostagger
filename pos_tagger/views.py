from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json as simplejson
from .models import Sentences, Sentence_Tag, Tags
from .service import save_word, generate_tags, create_super_user
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Count
from django.http import HttpResponse
from django.db.models.query import QuerySet
from .models import Sentences, Tags
from .service import save_word


# Create your views here.
# view function for saving form
@login_required()
@csrf_exempt
def home(request):
    pos_tagger_list = Tags.objects.all()
    context = {'pos_tagger_list': pos_tagger_list}
    if request.method == 'POST':
        data = simplejson.loads(request.POST['data'])
        for d in data:
            s = Sentences.objects.create(sentence=d['sentence'])
            [save_word(s, w) for w in d['word'] if w.get('tag')]
        # messages.success(request, 'Student created successfully.')
        return JsonResponse(simplejson.dumps({'results': 'Your Selected Pos is Tagged Successfully'}), safe=False)
    return render(request, 'home.html', context)


def about(request):
    pos_tagger_list = Tags.objects.all()
    context = {'pos_tagger_list': pos_tagger_list}
    return render(request, 'about.html', context)


def contact(request):
    pos_tagger_list = Tags.objects.all()
    context = {'pos_tagger_list': pos_tagger_list}
    return render(request, 'contact.html', context)


def resource(request):
    pos_tagger_list = Tags.objects.all()
    context = {'pos_tagger_list': pos_tagger_list}
    return render(request, 'resource.html', context)


def stats(request):
    pos_tagger_list = Tags.objects.all()
    #pos=list()
    # query = Sentence_Tag.objects.all().query
    # query.group_by = ['tag_id']
    # results = QuerySet(query=query, model=Sentence_Tag)
    pos_counter=Sentence_Tag.objects.values('tag__name').annotate(count=Count('id'))
    tag_counter=list(pos_counter)
    # com=[]
    # for d in pos_tagger_list:
    #     for c in tag_counter:
    #         if d.id is c.tag_id:
    #             com.append(d.name)

    #print()
    # pos_tagger_count = Sentence_Tag.objects.all()
    # pos_counter =[566]
    # counter=0
    # for d in pos_tagger_list:
    #     for c in pos_tagger_count:
    #         if d['id'] == c.tag:
    #             counter+=1
    #     pos_counter.append(counter)
    #     counter=0
    context = {'pos_tagger_list': pos_tagger_list,'tag_counter': tag_counter}
    #return HttpResponse(simplejson.dumps(tag_counter), content_type="application/json")
    return render(request, 'stats.html', context)
