# Cartofriches - principaux endpoints

Permet d'interroger les friches et leurs géométries.

---

## 📂 `cartofriches.friches`

### Description

::: apifoncier.endpoints.cartofriches.CartofrichesEndpoint.friches

### Exemples d'utilisation

- Friches d'une commune :
  ```python
  # Initialisation du client
  from apifoncier import ApiFoncierClient
  
  client = ApiFoncierClient()

  # Requête pour les friches d'une commune
  friches = client.cartofriches.friches(code_insee="59350")
  ```

- Friches d'un département :
  ```python
  # Requête pour les friches d'un département
  friches = client.cartofriches.friches(coddep="62")
  ```

- Friches dans une emprise géographique :
  ```python
  # Requête pour les friches dans une emprise géographique
  friches = client.cartofriches.friches(in_bbox=[2.76, 49.73, 3.75, 50.6])
  ```

# Friches autour d'un point
```python
  # Requête pour les friches à proximité d'un point (emprise rectangulaire de 0.5° autour du point)
  client.cartofriches.friches(lon_lat=[2.8, 49.75])
```

- Friches avec filtres - surface entre 1000 et 5000 m², zone urbaine de type "U" :
  ```python
  # Friches avec filtres
  friches = client.cartofriches.friches(
      code_insee="59350",
      surface_min=1000,
      surface_max=5000,
      urba_zone_type="U",
      fields="all", # Récupère tous les champs disponibles
  )
  ```

---

## 📂 `cartofriches.geofriches`

### Description

::: apifoncier.endpoints.cartofriches.CartofrichesEndpoint.geofriches

### Exemples d'utilisation

- Friches géolocalisées d'une commune :
  ```python
  client.cartofriches.geofriches(code_insee="59001")
  ```
- Friches géolocalisées d'un département :
  ```python
  client.cartofriches.geofriches(coddep="62")
  ```
- Friches géolocalisées avec filtre sur zone urbaine :
  ```python
  client.cartofriches.geofriches(code_insee="59001", urba_zone_type="U")
  ```

---

## 📂 `cartofriches.friche_by_id`

### Description

::: apifoncier.endpoints.cartofriches.CartofrichesEndpoint.friche_by_id

### Exemples d'utilisation

- Friche par identifiant :
  ```python
  client.cartofriches.friche_by_id(site_id="FR123456")
  ```
