
import urllib.request, json

urltoparse = "https://api.stores.sainsburys.co.uk/v1/stores/?api_client_id=LocPropAspire&fields=name,total_square_feet&limit=50&page="
pages = 65

def parseaway():
    x = 1
    count = 0
    storeToSize = {}
    while x <= pages:
        with urllib.request.urlopen(urltoparse+str(x)) as url:
            data = json.loads(url.read().decode())
            for store in data['results']:
                try:
                    storeToSize[str(store['name'])] = int(store['total_square_feet'])
                except:
                    storeToSize[str(store['name'])] = 0
                count = count+1
        x = x+1
    done_sorting = sorted(storeToSize.items(), key=lambda i: i[1])

    print(done_sorting[len(done_sorting)-1])
    print("\n Total Stores:" + str(count))


if __name__ == "__main__":
    parseaway()
