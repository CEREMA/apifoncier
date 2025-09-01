# Fichiers Fonciers - principaux endpoints

Permet d'interroger les parcelles, locaux, TUPs, droits de propriété et leurs géométries.


## Clef API

Une clé API est requise pour accéder aux endpoints FF. Vous pouvez obtenir une clé via le [Portail Données foncières](https://portaildf.cerema.fr).

```python
from apifoncier.client import ApiFoncierClient

api_key = "VOTRE_CLE_API"  # Clé API requise pour accéder aux endpoints FF
client = ApiFoncierClient({"api_key": api_key})
```

---

## 📂 `ff.parcelles`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.parcelles

### Exemples d'utilisation

- Parcelles d'une commune :
```python
client.ff.parcelles(code_insee="59001")
```
- Parcelles dans une emprise géographique :
```python
client.ff.parcelles(in_bbox=[2.76, 49.73, 2.779, 49.749])
```
- Parcelles avec plusieurs codes INSEE et une surface minimale de 1000 m² :
```python
client.ff.parcelles(codes_insee=["59001", "59002"], dcntpa_min=1000)
```
- Parcelles avec filtre centrée sur une coordonnée (lon, lat) :
```python
client.ff.parcelles(lon_lat=[2.76, 49.73])
```

- Parcelles appartenant à des propriétaires personnes physiques (catpro3="X"), avec au moins un local (nlocal_min=1) et construites après 2010 (jannatmin_min=2010) dans la commune dont le code insee est 59001 :
```python
client.ff.parcelles(code_insee="59001", catpro3="X", nlocal_min=1, jannatmin_min=2010)
```

---

## 📂 `ff.parcelle_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.parcelle_by_id

### Exemples d'utilisation

- Parcelle par identifiant :
```python
client.ff.parcelle_by_id("590010000U1186")
```

---

## 📂 `ff.geoparcelles`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.geoparcelles

### Exemples d'utilisation

- Parcelles géolocalisées d'une commune :
```python
client.ff.geoparcelles(code_insee="59001")
```
- Parcelles géolocalisées dans une emprise :
```python
client.ff.geoparcelles(in_bbox=[2.76, 49.73, 2.779, 49.749])
```
- Parcelles géolocalisées avec un propriétaire public :
```python
client.ff.geoparcelles(code_insee="59001", catpro3="P")
```

---

## 📂 `ff.locaux`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.locaux

### Exemples d'utilisation

- Locaux d'une commune :
```python
client.ff.locaux(code_insee="59001")
```
- Locaux de type "appartement" (dteloc="2") dans la commune de Lille (59350) avec une surface minimale de 180 m² :
```python
client.ff.locaux(code_insee="59350", dteloc="2", slocal_min=180)
```

---

## 📂 `ff.local_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.local_by_id

### Exemples d'utilisation

- Local par identifiant :
```python
client.ff.local_by_id(idlocal="592980433303")
```

---

## 📂 `ff.tups`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.tups

### Exemples d'utilisation

- TUPs d'une commune :
```python
client.ff.tups(code_insee="59001")
```
- TUPs de type "unité foncière" (typetup="UF") appartenant à des propriétaires publics (catpro3="P") :
```python
client.ff.tups(code_insee="59001", typetup="UF", catpro3="P")
```
- TUPs avec plusieurs identifiants :
```python
client.ff.tups(bbox=[2.76, 49.73, 2.779, 49.749], )
```

---

## 📂 `ff.tup_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.tup_by_id

### Exemples d'utilisation

- TUP par identifiant :
```python
client.ff.tup_by_id("uf590010396107")
```

---

## 📂 `ff.geotups`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.geotups

### Exemples d'utilisation

- TUPs géolocalisées d'une commune :
```python
client.ff.geotups(code_insee="59001")
```
- TUPs géolocalisées avec filtre propriétaire :
```python
client.ff.geotups(code_insee="59001", catpro3="P")
```

---

## 📂 `ff.proprios`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.proprios

### Exemples d'utilisation

- Droits de propriété d'une commune :
```python
client.ff.proprios(code_insee="59001")
```
- Droits de propriété avec filtre sur catégorie publique :
```python
client.ff.proprios(code_insee="59001", catpro3="P")
```
- Droits de propriété avec droit de propriété de type GERANT,MANDATAIRE (ccodro) :
```python
client.ff.proprios(code_insee="59001", ccodro="G", fields="all")
```

---

## 📂 `ff.proprio_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.proprio_by_id

### Exemples d'utilisation

- Droit de propriété par identifiant :
```python
client.ff.proprio_by_id(idprodroit="59001D0017702")
```

