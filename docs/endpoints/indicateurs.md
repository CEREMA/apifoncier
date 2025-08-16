# Indicateurs - principaux endpoints

Permet d'interroger les indicateurs de consommation d'espace, d'accessibilité, d'activité, de prix et de valorisation.

---

## 📂 `indicateurs.conso`

### Description

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.conso

### Exemples d'utilisation

- Consommation d'espace pour une commune :
  ```python
  client.indicateurs.conso(code="59001", echelle="communes")
  ```
- Consommation d'espace pour un département :
  ```python
  client.indicateurs.conso(code="62", echelle="departements")
  ```
- Consommation d'espace sur une période :
  ```python
  client.indicateurs.conso(code="59001", echelle="communes", annee_min=2015, annee_max=2022)
  ```
- Consommation d'espace avec tri :
  ```python
  client.indicateurs.conso(code="59001", echelle="communes", ordering="-annee")
  ```

---

## 📂 `indicateurs.accessibilite`

### Description

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.accessibilite

### Exemples d'utilisation

- Accessibilité pour une AAV :
  ```python
  client.indicateurs.accessibilite(codes_aav="AAV123")
  ```
- Accessibilité pour plusieurs AAV :
  ```python
  client.indicateurs.accessibilite(codes_aav=["AAV123", "AAV456"])
  ```
- Accessibilité pour une année donnée :
  ```python
  client.indicateurs.accessibilite(codes_aav="AAV123", annee="2021")
  ```

---

## 📂 `indicateurs.activite`

### Description

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.activite

### Exemples d'utilisation

- Activité pour une commune :
  ```python
  client.indicateurs.activite(codes="59001", echelle="communes")
  ```
- Activité pour un EPCI :
  ```python
  client.indicateurs.activite(codes="200066010", echelle="epci")
  ```
- Activité pour plusieurs codes :
  ```python
  client.indicateurs.activite(codes=["59001", "67890"], echelle="communes")
  ```

---

## 📂 `indicateurs.prix`

### Description

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.prix

### Exemples d'utilisation

- Prix annuel pour une commune :
  ```python
  client.indicateurs.prix(codes="59001", echelle="communes", type_prix="annuel")
  ```
- Prix triennal pour un département :
  ```python
  client.indicateurs.prix(codes="62", echelle="departements", type_prix="triennal")
  ```
- Prix avec tri et année :
  ```python
  client.indicateurs.prix(codes="59001", echelle="communes", ordering="-annee", annee="2022")
  ```

---

## 📂 `indicateurs.valorisation`

### Description

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.valorisation

### Exemples d'utilisation

- Valorisation pour une AAV :
  ```python
  client.indicateurs.valorisation(code="AAV123", echelle="aav")
  ```
- Valorisation pour un EPCI :
  ```python
  client.indicateurs.valorisation(code="200066010", echelle="epci")
  ```
- Valorisation pour une année donnée :
  ```python
  client.indicateurs.valorisation(code="AAV123", echelle="aav", annee="2021")
  ```
