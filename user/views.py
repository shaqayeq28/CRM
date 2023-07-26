from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from user.forms import SignUpForm, AddLeadForm
from user.models import UserProfile, Lead


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()

            return redirect('/log-in/')

    form = SignUpForm()

    return render(request, 'user/signup.html', context={'form': form})


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')


@login_required
def add_lead(request):
    if request.method == "POST":
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead_obj = Lead.objects.create(**form.cleaned_data, created_by=request.user)
            lead_obj.save()
            messages.success(request, "the lead created successfully")

            return redirect('leads_list')
    form = AddLeadForm()

    return render(request, 'user/add_lead.html', context={'form': form})


def leads_list(request):
    leads = Lead.objects.filter(is_active=True, created_by=request.user)
    return render(request, 'user/leads_list.html', context={'leads': leads})


@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, is_active=True, created_by=request.user, pk=pk)
    return render(request, 'user/leads_detail.html', context={'lead': lead})


@login_required
def delete_leads(request, pk):
    lead = get_object_or_404(Lead, is_active=True, created_by=request.user, pk=pk)
    lead.is_active = False

    messages.success(request, "the lead deleted successfully")
    return redirect('leads_list')


@login_required
def edit_leads(request, pk):
    lead = get_object_or_404(Lead, is_active=True, created_by=request.user, pk=pk)

    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "the lead edited successfully")

            return redirect('leads_list')

    form = AddLeadForm(instance=lead)

    return render(request, 'user/leads_edit.html', context={'form': form})
