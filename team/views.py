from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from team.forms import EditTeamForm
from team.models import Team


@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, is_active=True, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = EditTeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, "the team edited successfully")

            return redirect('my_profile')

    form = EditTeamForm(instance=team)

    return render(request, 'team/edit_team.html', context={'team': team, 'form': form})
