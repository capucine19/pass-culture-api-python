# pass-culture-api-python
Api de recherche du pass culture avancée

Cet outil permet de faire des recherches sur l'application pass culture de façon poussée.
en effet vous pouvez ajouter une liste de librairie et le nom d'un livre. Le programme va rechercher cet item dans tous les endroits demandés.
Le filtre est assez large : par exemple vous pouvez mettre *fnac paris* et la recherche va rechercher dans toutes les fnac de paris.


## Exemple n°1 rechercher un livre dans plusieurs librairies : 
![image](https://user-images.githubusercontent.com/44448753/162581122-bdc63e26-6d32-45f2-9d6d-37bc437348f8.png)
```python
liste = ['Smith & Son','Galignani','Gibert joseph paris','fnac paris']

recherche('Where the crawdads sing',liste,arround=False)       
```

## Exemple n°2 rechercher un livre partout autour d'une zone définie : 
![image](https://user-images.githubusercontent.com/44448753/162581223-d17b6ac4-5c4c-412e-8985-e18de8210221.png)

Le programme va recherche le livre *Where the crawdads sing* environ 60km autour de Marseille (semblable à une recherche 'autour de moi' sur l'application pass culture)

```python
liste=['Marseille']

recherche('Where the crawdads sing',liste,arround=True)       
```
Attention : Activez le mode **arround** avec arround = True quand il s'agit d'une ville 

## Lancer le script :

Seul les librairies json et requests sont nécéssaires (par défaut elles sont installées nativement sur python)
```python
pip install requests 
```
```python
pip install json
```
si jamais elles ne sont pas installées

## A propos :

Tous les token , liens api etc sont public en trifouillant le site du pass culture.

___
> url_pass = 'https://e2ikxj325n-dsn.algolia.net/1/indexes/PRODUCTION/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.11.0)%3B%20Browser'

--> api qui renvoie du json avec tous les items correspondant à une recherche. 
Requête en post avec comme paramètres les headers et un payload. 

**Exemple** : Pour récupérer les données de cette page https://passculture.app/recherche?showResults=true&query=%22where%20the%20crawdads%20sing%22&locationFilter=%7B%22locationType%22%3A%22AROUND_ME%22%2C%22aroundRadius%22%3A100%7D&offerCategories=%5B%5D&priceRange=%5B0%2C300%5D 

___
> url_lieux = 'https://e2ikxj325n-dsn.algolia.net/1/indexes/venues/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.11.0)%3B%20Browser'

--> api qui renvoie du json avec tous les lieux correspondant à une recherche. 
Requête en post avec comme paramètres les headers et un payload. 

**Exemple** : Pour récupérer les lieux comme ceci ![image](https://user-images.githubusercontent.com/44448753/162581747-120a71f6-523f-446d-8270-8f7a9d839193.png)

___
> url_item = 'https://backend.passculture.app/native/v1/offer/{id item}'

--> api qui permet de récupérer des informations sur une offre en insérant son id.

**Exemple** : https://backend.passculture.app/native/v1/offer/1124720 renvoie : 

```json
{'id': 1124720, 'accessibility': {'audioDisability': None, 'mentalDisability': None, 'motorDisability': None, 'visualDisability': None}, 'description': None, 'expenseDomains': ['all', 'physical'], 'externalTicketOfficeUrl': None, 'extraData': {'author': 'Owens, Delia', 'durationMinutes': None, 'isbn': '9780593085851', 'musicSubType': None, 'musicType': None, 'performer': None, 'showSubType': None, 'showType': None, 'stageDirector': None, 'speaker': None, 'visa': None}, 'isExpired': False, 'isForbiddenToUnderage': False, 'isReleased': True, 'isSoldOut': False, 'isDigital': False, 'isDuo': False, 'isEducational': False, 'name': 'WHERE THE CRAWDADS SING', 'stocks': [{'id': 1148398, 'beginningDatetime': None, 'bookingLimitDatetime': None, 'cancellationLimitDatetime': None, 'isBookable': True, 'isForbiddenToUnderage': False, 'isSoldOut': False, 'isExpired': False, 'price': 1460, 'activationCode': None}], 'subcategoryId': 'LIVRE_PAPIER', 'image': {'url': 'https://storage.googleapis.com/passculture-metier-prod-production-assets/thumbs/products/FKSYU', 'credit': None}, 'venue': {'id': 969, 'address': 'SQUARE MONSEIGNEUR ROULL', 'city': 'BREST', 'offerer': {'name': 'SA LIBRAIRIE DIALOGUES'}, 'name': 'Dialogues Brest', 'postalCode': '29200', 'publicName': None, 'coordinates': {'latitude': 48.38737, 'longitude': -4.49063}, 'isPermanent': True}, 'withdrawalDetails': None}
```
