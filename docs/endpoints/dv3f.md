# DV3F - principaux endpoints

Permet d'interroger les mutations DV3F et leurs géométries.

## Clef API

Une clé API est requise pour accéder aux endpoints DV3F. Vous pouvez obtenir une clé via le [Portail Données foncières](https://portaildf.cerema.fr).

```python
from apifoncier.client import ApiFoncierClient

api_key = "VOTRE_CLE_API"  # Clé API requise pour accéder aux endpoints DV3F
client = ApiFoncierClient({"api_key": api_key})
```

---

## 📂 `dv3f.mutations`

### Description

::: apifoncier.endpoints.dv3f.DV3FEndpoint.mutations

### Exemples d'utilisation

- Mutations DV3F pour une commune :
  ```python
  client.dv3f.mutations(code_insee="59001")
  ```

- Mutations DV3F dans une emprise géographique :
  ```python
  client.dv3f.mutations(in_bbox=[2.76, 49.73, 2.779, 49.749])
  ```

- Mutations DV3F pour plusieurs communes :
  ```python
  client.dv3f.mutations(codes_insee=["59001", "62001"])
  ```

- Mutations DV3F pour une commune donnée (ici, via le code INSEE 59350) en 2022, pour des biens de type maison ancienne(codtypbien=1113) et dont la surface est comprise entre 1000 et 5000 m2, en récupérant tous les champs disponibles :

```python
client.dvf_opendata.mutations(
    code_insee="59350",
    anneemut="2022",
    fields="all",
    sterr_min=1000,
    sterr_max=5000,
    codtypbien="1113",
)
```

---

## 📂 `dv3f.geomutations`

### Description

::: apifoncier.endpoints.dv3f.DV3FEndpoint.geomutations

### Exemples d'utilisation

- Mutations DV3F géolocalisées pour une commune :
  ```python
  client.dv3f.geomutations(code_insee="59001")
  ```
- Mutations DV3F géolocalisées dans une emprise :
  ```python
  client.dv3f.geomutations(in_bbox=[2.76, 49.73, 2.779, 49.749])
  ```
- Mutations DV3F géolocalisées filtrées par type de bien :
  ```python
  client.dv3f.geomutations(code_insee="59001", codtypbien="1113")
  ```

---

## 📂 `dv3f.mutation_by_id`

### Description

::: apifoncier.endpoints.dv3f.DV3FEndpoint.mutation_by_id

### Exemples d'utilisation

- Mutation DV3F par identifiant :
  ```python
  client.dv3f.mutation_by_id(idmutation=123456)
  ```
