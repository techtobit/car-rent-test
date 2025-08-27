from django.shortcuts import render, redirect
import django_tables2 as tables
from . import forms
from cars.models import Cars, Purchase
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from django.http import HttpResponseRedirect

class AddCar(CreateView):
    model = Cars
    form_class = forms.CarsFrom
    template_name = 'add_cars.html'
    success_url = reverse_lazy('add_cars')
    def form_valid(self, form):
        return super().form_valid(form)

class DetailPostView(DetailView):
    model = Cars
    context_object_name = 'car'
    pk_url_kwarg = 'id'
    template_name = 'detail_post.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse_lazy('detail_post', kwargs={'id': post.pk}))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def buy_car(request, id):
    try:
        car = Cars.objects.get(pk=id)
    except Cars.DoesNotExist:
        massages.error(request, 'Car not found')
        return redirect("home.html")
    car.reduced_quantity()
    car.save()
    data = Purchase.objects.create(user=request.user, car =car)
    # massages.success(request,'Car purchased successfully')
    return redirect('home')


def ProfileView(request):
    purchaseCar = Purchase.objects.all()
    car = []
    for data in purchaseCar:
        if data.id > 0 : 
            newArray = Cars.objects.get(pk=data.car.id)
            car.append(newArray)
    return render(request, 'profile.html', {'purchaseCar': car})
    



# class ProfileView(DetailView):
#     model = Purchase
#     template_name = 'profile.html'