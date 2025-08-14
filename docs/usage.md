# Usage

## Initialisation du client

```python
from apifoncier.client import ApiFoncierClient

config = {
    "api_key": "VOTRE_CLE_API",  # Facultatif pour les endpoints ouverts
    "base_url": "https://datafoncier.cerema.fr/api",
    "timeout": 10,
}

client = ApiFoncierClient(config)
```

## Exemple de requête

```python
# Endpoint ouvert
result = client.dvf_opendata.mutations(code_insee="12345")

# Endpoint restreint (clé API requise)
result = client.ff.parcelles(code_insee="12345")
```

## Utilisation avec le contexte

```python
with ApiFoncierClient(config) as client:
    data = client.cartofriches.friches(code_insee="12345")
```

## Format des résultats

- Par défaut : pandas.DataFrame
- Option : liste de dictionnaires (`format_output="dict"`)

## Pagination

La pagination est gérée automatiquement par défaut (`paginate=True`).  
Vous pouvez désactiver la pagination ou ajuster la taille de page avec `page_size`.

## Documentation des endpoints

Consultez les fiches dédiées pour chaque endpoint dans la section "Endpoints" de la documentation.
