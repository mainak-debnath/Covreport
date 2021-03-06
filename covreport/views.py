from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "key",
    'x-rapidapi-host': "host"
}

response = requests.request("GET", url, headers=headers).json()


# Create your views here.


def covidData(request):
    noofresults = int(response['results'])
    mylist = []
    for x in range(noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        for x in range(noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)
        context = {'selectedcountry': selectedcountry, 'mylist': mylist, 'new': new, 'active': active,
                   'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}

        return render(request, 'index.html', context)

    context = {'mylist': mylist}
    return render(request, 'index.html', context)
