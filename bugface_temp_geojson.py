def get_lat_lng_capital():
    import random
    import urllib.request, urllib.parse, urllib.error
    import json
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

    capitals =['Kabul','Tirana','Algiers','Luanda','Yerevan','Canberra','Vienna','Baku','Nassau',
               'Manama','Dhaka','Bridgetown','Minsk','Brussels','Belmopan','Porto-Novo','Thimphu',
               'Sarajevo','Gaborone','Brasilia','Sofia','Ouagadougou','Bujumbura']
    max_len = len(capitals)
    rand_capital = random.randint(0, (max_len - 1))
    address = capitals[rand_capital]

    url = serviceurl + urllib.parse.urlencode({'address': address})
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        return 'Fail'

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js['results'][0]['formatted_address']
    return 'Capital: '+location+'\nlat: '+str(lat)+' lng: '+str(lng)


print(get_lat_lng_capital())

