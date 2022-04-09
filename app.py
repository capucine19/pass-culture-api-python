import requests
import json

#######################################################################################
# VARIABLES
#######################################################################################

headers = {
    'x-algolia-agent': 'Algolia for JavaScript (3.35.1); Browser; JS Helper (3.1.0)',
    'x-algolia-application-id': 'E2IKXJ325N',
    'x-algolia-api-key':'5743d3e703bf3aade8da0b12e8f67fb9'        
}
url_pass = 'https://e2ikxj325n-dsn.algolia.net/1/indexes/PRODUCTION/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.11.0)%3B%20Browser'
url_lieux = 'https://e2ikxj325n-dsn.algolia.net/1/indexes/venues/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.11.0)%3B%20Browser'
url_item = 'https://backend.passculture.app/native/v1/offer/'

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#######################################################################################
# FONCTIONS
#######################################################################################

def requete_pass(query,arround,liste_lieux,lieu):
    if arround == True:
        payload = {"query":query,"page":0,"hitsPerPage":999,"facetFilters":[["offer.isEducational:false"]],"numericFilters":[["offer.prices: 0 TO 300"]],"aroundLatLng":"{}, {}".format(liste_lieux[0]['geoloc']['lat'],liste_lieux[lieu]['geoloc']['lng']),"aroundRadius":100000,"attributesToRetrieve":["offer.dates","offer.isDigital","offer.isDuo","offer.isEducational","offer.name","offer.prices","offer.subcategoryId","offer.thumbUrl","objectID","_geoloc"],"attributesToHighlight":[]}
    else:
        payload = {"query":query,"page":0,"hitsPerPage":999,"facetFilters":[["offer.isEducational:false"],['venue.id:{0}'.format(lieu)]],"numericFilters":[["offer.prices: 0 TO 300"]],"attributesToRetrieve":["offer.dates","offer.isDigital","offer.isDuo","offer.isEducational","offer.name","offer.prices","offer.subcategoryId","offer.thumbUrl","objectID","_geoloc"],"attributesToHighlight":[]}
    r =requests.post(url_pass,headers=headers,data=json.dumps(payload))
    return r.json()

def requete_lieux(liste,arround):
    liste_lieux={}
    for a in range(len(liste)):
        payload = {"query":liste[a],"hitsPerPage":999,"attributesToHighlight":[]}
        r =requests.post(url_lieux,headers=headers,data=json.dumps(payload))
        data = r.json()
        if arround == True:
            liste_lieux[0] = {"name":data['hits'][0]['name'],"city":data['hits'][0]['city'],"type":data['hits'][0]['venue_type'],"geoloc":data['hits'][0]['_geoloc']}
        else:
            for b in range(data['nbHits']):
                liste_lieux[data['hits'][b]['objectID']] = {"name":data['hits'][b]['name'],"city":data['hits'][b]['city'],"type":data['hits'][b]['venue_type'],"geoloc":data['hits'][b]['_geoloc']}

    return liste_lieux   

def recherche(query,liste_lieux,arround):
    liste_lieux = requete_lieux(liste_lieux,arround)
    if arround==True:
        last_name = 0
        print(f'{colors.UNDERLINE}{colors.OKBLUE} ================> Recherche {query}...... proche de la position {liste} <================{colors.ENDC}{colors.ENDC}')
        data = requete_pass(query,arround,liste_lieux,lieu=False)
        for b in range(data['nbHits']):
            r_item = requests.get(f"{url_item}{data['hits'][b]['objectID']}")
            data_item = r_item.json()
            if data_item['venue']['name'] != last_name:
                print(f"{colors.OKGREEN}=============> {data_item['venue']['name']} ({data_item['venue']['city']}) {colors.ENDC}")
            else:
                pass
            last_name=data_item['venue']['name']
            print(f"- {colors.BOLD}{colors.OKCYAN} {data['hits'][b]['offer']['name']} {colors.ENDC} --> {data['hits'][b]['offer']['prices'][0]} euros{colors.ENDC}")
    else:
        print(f'{colors.UNDERLINE}{colors.OKBLUE} ================> Recherche {query}...... dans {len(liste_lieux)} lieux  <================{colors.ENDC}{colors.ENDC}')
        for lieu in liste_lieux:
            data = requete_pass(query,arround,liste_lieux,lieu)
            print('\n')
            if data['nbHits'] == 0:
                print(f"{colors.FAIL}=============> {liste_lieux[lieu]['name']} ({liste_lieux[lieu]['city']}) ----> {data['nbHits']} résultats{colors.ENDC}")
            else:
                print(f"{colors.OKGREEN}=============> {liste_lieux[lieu]['name']} ({liste_lieux[lieu]['city']}) ----> {data['nbHits']} résultats{colors.ENDC}")
            print('\n')
            for b in range(data['nbHits']):
                print(f"- {colors.BOLD}{colors.OKCYAN} {data['hits'][b]['offer']['name']} {colors.ENDC} --> {data['hits'][b]['offer']['prices'][0]} euros{colors.ENDC}")


                
                
                
#exemples               
liste = ['Smith & Son','Galignani','Gibert joseph paris','fnac paris'] #- <-- listes les librairies dans le quel chercher votre livre ou objet
#liste=['Marseille'] <-- Pour les villes activer le mode arround si dessous en méttant arround=true
recherche('Where the crawdads sing',liste,arround=False)       


