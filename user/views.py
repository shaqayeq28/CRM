from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from team.models import Team
from user.forms import SignUpForm, AddLeadForm, AddClientForm
from user.models import UserProfile, Lead, Client

#TODO: add admin field who can add leads and clients to teams

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
def my_profile(request):
    team = Team.objects.filter(created_by=request.user)
    return render(request, 'user/profile.html', context={'team': team})


@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)
    leads = Lead.objects.filter(team=team,
                                created_by=request.user,
                                converted_to_client=False).order_by('-created_time')[:5]
    clients = Client.objects.filter(team=team, created_by=request.user).order_by('-created_time')[:5]

    return render(request, 'user/dashboard.html', context={'leads': leads, 'clients': clients})


@login_required
def add_lead(request):
    team = Team.objects.filter(created_by=request.user)
    if request.method == "POST":

        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead_obj = Lead.objects.create(**form.cleaned_data, created_by=request.user, team=team)
            lead_obj.save()
            messages.success(request, "the lead created successfully")

            return redirect('leads_list')
    form = AddLeadForm()

    return render(request, 'user/add_lead.html', context={'form': form, 'team': team})


def leads_list(request):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'converted_to_client': False
    }
    leads = Lead.objects.filter(**filter_kwargs)
    return render(request, 'user/leads_list.html', context={'leads': leads})


@login_required
def leads_detail(request, pk):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'converted_to_client': False,
        'pk': pk
    }
    lead = get_object_or_404(Lead, **filter_kwargs)
    return render(request, 'user/leads_detail.html', context={'lead': lead})


@login_required
def delete_leads(request, pk):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'converted_to_client': False,
        'pk': pk
    }
    lead = get_object_or_404(Lead, **filter_kwargs)
    lead.is_active = False

    messages.success(request, "the lead deleted successfully")
    return redirect('leads_list')


@login_required
def edit_leads(request, pk):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'converted_to_client': False,
        'pk': pk
    }
    lead = get_object_or_404(Lead, **filter_kwargs)

    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "the lead edited successfully")

            return redirect('leads_list')

    form = AddLeadForm(instance=lead)

    return render(request, 'user/leads_edit.html', context={'form': form})


@login_required
def convert_lead_to_client(request, pk):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'converted_to_client': False,
        'pk': pk
    }
    team = Team.objects.filter(created_by=request.user)
    lead = get_object_or_404(Lead, **filter_kwargs)
    client = Client.objects.create(name=lead.name,
                                   email=lead.email,
                                   description=lead.description,
                                   created_by=request.user,
                                   team=team, )

    lead.converted_to_client = True
    lead.save(update_fields=['converted_to_client'])

    messages.success(request, "the lead converted to client")

    return redirect('leads_list')


@login_required
def clients_list(request):
    clients = Client.objects.filter(is_active=True, created_by=request.user)
    return render(request, 'user/clients_list.html', context={'clients': clients})


@login_required
def clients_detail(request, pk):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'pk': pk
    }
    client = get_object_or_404(Client, **filter_kwargs)
    return render(request, 'user/clients_detail.html', context={'client': client})


@login_required
def add_client(request):
    team = Team.objects.filter(created_by=request.user)
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            client_obj = Client.objects.create(**form.cleaned_data, created_by=request.user, team=team)
            client_obj.save()
            messages.success(request, "the client created successfully")

            return redirect('clients_list')
    form = AddClientForm()

    return render(request, 'user/clients_add.html', context={'form': form, 'team': team})


@login_required
def delete_client(request, pk):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'pk': pk
    }
    client = get_object_or_404(Client, **filter_kwargs)
    client.is_active = False

    messages.success(request, "the client deleted successfully")
    return redirect('clients_list')


@login_required
def edit_clients(request, pk):
    filter_kwargs = {
        'is_active': True,
        'created_by': request.user,
        'pk': pk
    }
    client = get_object_or_404(Client, **filter_kwargs)

    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "the client edited successfully")

            return redirect('clients_list')

    form = AddClientForm(instance=client)

    return render(request, 'user/clients_edit.html', context={'form': form})
