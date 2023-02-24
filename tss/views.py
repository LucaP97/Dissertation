from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
import http.client
import config
# recommender imports
import matplotlib.pyplot as plt
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

def home(request):

    key = config.football_api_key

    return render(request, "tss/home.html", {'key': key})

def about(request):
    return render(request, "tss/about.html")

def contact(request):
    return render(request, "tss/contact.html")

def api_example(request):

    rapid_api = config.rapid_api_key

    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': rapid_api
    }

    response = requests.get(conn.request("GET", "/teams?id=33", headers=headers))

    if response.status_code == 200:
        res = conn.getresponse()
        data = res.read()
        return render(request, 'members/select_team.html', {'data': data})
    else:
        return render(request, 'members/select_team.html', {'error': response.status_code})
    

def recommender(request):
    pass