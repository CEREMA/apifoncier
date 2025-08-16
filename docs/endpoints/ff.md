# Fichiers Fonciers - principaux endpoints

Permet d'interroger les parcelles, locaux, TUPs, droits de propriété et leurs géométries.

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
- Parcelles avec plusieurs codes INSEE :
```python
client.ff.parcelles(codes_insee=["59001", "67890"])
```
- Parcelles avec filtre sur la surface :
```python
client.ff.parcelles(code_insee="59001", dcntpa_min=1000)
```

---

## 📂 `ff.parcelle_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.parcelle_by_id

### Exemples d'utilisation

- Parcelle par identifiant :
```python
client.ff.parcelle_by_id(idparcelle="123456789A")
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
- Parcelles géolocalisées avec filtre propriétaire :
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
- Locaux avec filtre sur type de local :
```python
client.ff.locaux(code_insee="59001", dteloc="MAISON,APPARTEMENT")
```
- Locaux avec surface minimale :
```python
client.ff.locaux(code_insee="59001", slocal_min=50)
```

---

## 📂 `ff.local_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.local_by_id

### Exemples d'utilisation

- Local par identifiant :
```python
client.ff.local_by_id(idlocal="987654321")
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
- TUPs avec filtre sur type :
```python
client.ff.tups(code_insee="59001", typetup="SIMPLE")
```
- TUPs avec plusieurs identifiants :
```python
client.ff.tups(idtup=["TUP123456", "TUP654321"])
```

---

## 📂 `ff.tup_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.tup_by_id

### Exemples d'utilisation

- TUP par identifiant :
```python
client.ff.tup_by_id(idtup="TUP123456")
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
- Droits de propriété avec filtre sur catégorie :
```python
client.ff.proprios(code_insee="59001", catpro3="P")
```
- Droits de propriété avec type de droit :
```python
client.ff.proprios(code_insee="59001", typedroit="propriétaire")
```

---

## 📂 `ff.proprio_by_id`

### Description

::: apifoncier.endpoints.ff.FFEndpoint.proprio_by_id

### Exemples d'utilisation

- Droit de propriété par identifiant :
```python
client.ff.proprio_by_id(idprodroit="PRO123456")
```

