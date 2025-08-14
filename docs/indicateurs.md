# Indicateurs - principaux endpoints

Permet d'interroger les indicateurs de consommation d'espace, d'accessibilité, d'activité, de prix et de valorisation.

## Méthodes principales

### `conso`

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.conso

```python
client.indicateurs.conso(code="12345", echelle="communes")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `accessibilite`

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.accessibilite

```python
client.indicateurs.accessibilite(codes_aav="AAV123")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `activite`

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.activite

```python
client.indicateurs.activite(codes="12345", echelle="communes")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `prix`

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.prix

```python
client.indicateurs.prix(codes="12345", echelle="communes", type_prix="annuel")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict

### `valorisation`

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.valorisation

```python
client.indicateurs.valorisation(code="AAV123", echelle="aav")
```
**Filtre fields** : `all` pour obtenir tous les champs, `None` sinon  
**Retour** : DataFrame ou liste de dict
