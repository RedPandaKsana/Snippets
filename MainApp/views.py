from django.http import Http404
from django.shortcuts import render, redirect
from .models import Snippet
from .forms import SnippetForm, CommentForm, UserRegistrationForm
from django.contrib import auth


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm()
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)  # то есть не добавили в бд
            if request.user.is_authenticated:
                snippet.user = request.user
            snippet.save() #а вот тут уже добавили
            return redirect('/thanks')
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm(request.POST)
        print("errors = ", form.errors)
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = get_base_context(request, 'Просмотр сниппетов')
    snippets = Snippet.objects.all()
    context["snippets"] = snippets
    #print("context = ", context)
    return render(request, 'pages/view_snippets.html', context)

#def items(request):
#    items = Snippet.objects.all()
#    print(items)
#    return render(request, "pages/view_snippets.html", {"items": items})

def snippet(request, snippet_id):
    context = get_base_context(request, "Страница сниппета")
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        #comments = snippet.comment_set.all()
    except Snippet.DoesNotExist:
        raise Http404

    context["comment_form"] = CommentForm() # передали форму от комментов
    #context["comments"] = comments
    context["snippet"] = snippet
    return render(request, "pages/snippet.html", context)

#def add_form(request):
#    if request.method == "POST":
#        form = SnippetForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('/')

def thanks(request):
    context = get_base_context(request, 'Thanks!!!')
    return render(request, 'pages/thanks.html', context)

def login_page(request):
    context = get_base_context(request, 'Login')
    return render(request, 'pages/login.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        #if user is not None:
        #    auth.login(request, user)
        #else:
           # Return error message
        #    pass
        errors = ["Некорректные данные!", ]
        context = get_base_context(request, 'Login')
        context["errors"] = errors
        context["username"] = username
        return render(request, 'pages/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('main_page')

def delete(request, delete_id):
    snippet = Snippet.objects.get(id=delete_id)
    snippet.delete()
    return redirect('main_page')

def edit(request, id):
    try:
        snippet = Snippet.objects.get(id=id)

        if request.method == "POST":
            snippet.name = request.POST.get("name")
            snippet.lang = request.POST.get("lang")
            snippet.code = request.POST.get("code")
            snippet.save()
            return redirect("/")
        elif request.method == "GET":
            return render(request, "pages/edit.html", {"snippet": snippet})
    except Snippet.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def comment_add(request):
   if request.method == "POST":
       snippet_id = request.POST["snippet_id"]
       comment_form = CommentForm(request.POST)
       if comment_form.is_valid():
           comment = comment_form.save(commit=False)
           comment.author = request.user
           snippet = Snippet.objects.get(id=snippet_id)
           comment.snippet = snippet
           comment.save()

       return redirect(f'/snippet/{snippet_id}')

   raise Http404

def my_snippets(request):
    context = get_base_context(request, "Мои сниппеты")
    if request.user.is_authenticated:
        snippets = Snippet.objects.filter(user=request.user)
        context["snippets"] = snippets
        return render(request, 'pages/my_snippets.html', context)
    else:
        return redirect('/login/')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, '/', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/register.html', {'user_form': user_form})