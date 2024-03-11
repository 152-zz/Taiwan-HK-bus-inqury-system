import requests
#address
def HK_bus(busroute = 'A28',direction = 'inbound'):
    route_url = 'https://rt.data.gov.hk/v2/transport/citybus/route/CTB/'+busroute
    # Parameters
    params = {    
        # the direction
        'direction': 'inbound',  
    }
    response = requests.get(route_url, params=params)
    # 200 means successful connection
    if response.status_code == 200:
        route_data = response.json()
        print(route_data)
        Q1 = route_data #利用Route API检索公交路线A28的路线信息。
    else:
        print("Fail to connection:", response.status_code)
        Q1 = 0

    # Endpoint for the Route API (replace this with the actual Route API endpoint from the documentation)
    route_api_url = 'https://rt.data.gov.hk/v2/transport/citybus/route-stop/CTB/'+busroute+'/'+direction

    # Make the request
    response = requests.get(route_api_url)#, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        route_data = response.json()
        print(route_data)
    else:
        print("Failed to retrieve data:", response.status_code)

    import json
    url2 = "https://rt.data.gov.hk/v2/transport/citybus/route-stop/CTB/"+busroute+'/'+direction
    response2 = requests.get(url2)
    text_content2 = response2.text
    print(text_content2)

    content2_json = json.loads(text_content2)

    # extract data
    stop = [item["stop"] for item in content2_json["data"]]
    print("Stop IDs:", stop)

    url3 = "https://rt.data.gov.hk/v2/transport/citybus/stop/{stop_id}"
    Q2 = []
    for stop_id in stop:
        url31 = url3.format(stop_id=stop_id)
        response3 = requests.get(url31)
        text_content3 = response3.text
        content3_json = json.loads(text_content3)

        stop_temp = content3_json["data"]["stop"]
        name_tc = content3_json["data"]["name_tc"]
        print("Stop ID:", stop_temp, " Name tc:", name_tc)
        Q2.append([stop_temp,name_tc])
    return Q1,Q2

    '''
    for stop_id in stop:
        url31 = url3.format(stop_id=stop_id)
        response3 = requests.get(url31)
        text_content3 = response3.text
        content3_json = json.loads(text_content3)
        stop_temp = content3_json["data"]["stop"]
        name_tc = content3_json["data"]["name_tc"]
        if name_tc == "將軍澳站, 寶邑路":
            print("Stop ID:", stop_temp, " Name tc:", name_tc)
            break
    '''
def coming_bus(idx = '001825',busroute='A28'):
    import json
    url4 = ("https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/"+idx+'/'+busroute)
    response4 = requests.get(url4)
    text_content4 = response4.text
    content4_json = json.loads(text_content4)

    eta = content4_json["data"][0]["eta"]
    print("Estimated time of arrival for the next bus at the stop:", eta)
    return eta

Q1,Q2 = HK_bus()
Q3 = coming_bus()
print(Q1)
print(Q2)
print(Q3)

