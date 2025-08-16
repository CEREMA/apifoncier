# Usage

## Initialisation du client

```python
from apifoncier.client import ApiFoncierClient

config = {
    "api_key": "VOTRE_CLE_API",  # Facultatif - uniquement pour l'utilisation des endpoints restreints
    "progress_bar": False,  # Afficher la barre de progression (True/False - True par défaut)
}

client = ApiFoncierClient(config)
```

## Exemple de requête

```python
# Endpoint ouvert
result = client.dvf_opendata.mutations(code_insee="59001")

# Endpoint restreint (clé API requise)
result = client.ff.parcelles(code_insee="62001")
```

## Utilisation avec le contexte

```python
with ApiFoncierClient(config) as client:
    data = client.cartofriches.friches(code_insee="62001")
```

## Format des résultats

- Par défaut, le format renvoyé est un DataFrame pandas ou GeoDataFrame geopandas (`format_output="dataframe"`) .
- Les données peuvent également être récupérées sous la forme d'une liste de dictionnaires (`format_output="dict"`)

## Pagination

La pagination est gérée automatiquement. Par défaut (`paginate=True`), toutes les pages sont interrogées.

Vous pouvez désactiver la pagination (`paginate=False`) pour renvoyer uniquement la première page et ajuster la taille de page avec `page_size`.

## Documentation des endpoints

Consultez les fiches dédiées pour chaque endpoint dans la section "Endpoints" de la documentation.
