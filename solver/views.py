from django.shortcuts import render
from django.views import View
from .utils import solve_analogy_problem

class Index(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        w1 = request.POST.get('w1')
        w2 = request.POST.get('w2')
        w3 = request.POST.get('w3')

        if not (w1 and w2 and w3):
            return render(request, "index.html", {"error": "Please fill all the details"})

        results = solve_analogy_problem(w1, w2, w3)

        data = {
            "has_result":True,
            "results": results,
            "word1": w1,
            "word2": w2,
            "word3": w3,
        }
        return render(request, "index.html", data)

