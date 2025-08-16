# DVF Open Data - principaux endpoints

Permet d'interroger les mutations DVF+ et leurs géométries.


## 📂 `dvf_opendata.mutations`

### Description

::: apifoncier.endpoints.dvf_opendata.DVFOpenDataEndpoint.mutations

### Exemple d'utilisation

- Interroger les mutations DVF+ pour une commune donnée (ici, via le code INSEE 59001) :

```python
from apifoncier import ApiFoncierClient

client = ApiFoncierClient()
mutations = client.dvf_opendata.mutations(code_insee="59001")
```

- Interroger les mutations DVF+ dans une emprise geographique (ici, un rectangle défini par ses coordonnées) :

```python
client = ApiFoncierClient()
mutations = client.dvf_opendata.mutations(in_bbox=[2.76, 49.73, 2.779, 49.749])
```

--- 

## 📂 `dvf_opendata.geomutations`

### Description

::: apifoncier.endpoints.dvf_opendata.DVFOpenDataEndpoint.geomutations

### Exemple d'utilisation

- Interroger, sous forme d'un geodataframe, les mutations DVF+ pour une commune donnée (ici, via le code INSEE 59001) :

```python
from apifoncier import ApiFoncierClient

client = ApiFoncierClient()
client.dvf_opendata.geomutations(code_insee="59001")
```
