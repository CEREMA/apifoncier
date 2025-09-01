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

- Interroger les mutations DVF+ pour une commune donnée (ici, via le code INSEE 59350) en 2022, pour des biens de type maison (codtypbien=111) et dont la surface est comprise entre 1000 et 5000 m2, en récupérant tous les champs disponibles :

```python
client.dvf_opendata.mutations(
    code_insee="59350",
    anneemut="2022",
    fields="all",
    sterr_min=1000,
    sterr_max=5000,
    codtypbien="111",
)
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

- Interroger, sous forme d'un geodataframe, les mutations DVF+ pour plusieurs communes (ici, via les codes INSEE 59350 et 59009), en 2023, pour des biens de type appartement (codtypbien=121) et dont la surface bâtie est supérieure à 100 m2 :

```python
client.dvf_opendata.geomutations(
    codes_insee=["59350", "59009"],
    sbati_min=100,
    anneemut=2023,
    codtypbien="121",
)
```