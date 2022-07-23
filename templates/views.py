from django.shortcuts import render


def submit_midi(request):
    if request.method == "POST":
        data = "Success"
        print("SUCCESS")
        return render(request, 'index.html', {'data': data})
