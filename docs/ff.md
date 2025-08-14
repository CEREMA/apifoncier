# Fichiers Fonciers - principaux endpoints

Permet d'interroger les parcelles, locaux, TUPs, droits de propriété et leurs géométries.

## Méthodes principales

### `parcelles`

::: apifoncier.endpoints.ff.FFEndpoint.parcelles

```python
client.ff.parcelles(code_insee="12345")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `parcelle_by_id`

::: apifoncier.endpoints.ff.FFEndpoint.parcelle_by_id

```python
client.ff.parcelle_by_id(idparcelle="123456789A")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : dict

### `geoparcelles`

::: apifoncier.endpoints.ff.FFEndpoint.geoparcelles

```python
client.ff.geoparcelles(code_insee="12345")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : GeoDataFrame

### `locaux`

::: apifoncier.endpoints.ff.FFEndpoint.locaux

```python
client.ff.locaux(code_insee="12345")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `local_by_id`

::: apifoncier.endpoints.ff.FFEndpoint.local_by_id

```python
client.ff.local_by_id(idlocal="987654321")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : dict

### `tups`

::: apifoncier.endpoints.ff.FFEndpoint.tups

```python
client.ff.geotups(code_insee="12345")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `tup_by_id`

::: apifoncier.endpoints.ff.FFEndpoint.tup_by_id

```python
client.ff.tup_by_id(idtup="TUP123456")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : dict

### `geotups`

::: apifoncier.endpoints.ff.FFEndpoint.geotups

```python
client.ff.geotups(code_insee="12345")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : GeoDataFrame

### `proprios`

::: apifoncier.endpoints.ff.FFEndpoint.proprios

```python
client.ff.proprios(code_insee="12345")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `proprio_by_id`

::: apifoncier.endpoints.ff.FFEndpoint.proprio_by_id

```python
client.ff.proprio_by_id(idprodroit="PRO123456")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : dict

