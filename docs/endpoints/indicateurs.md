# Indicateurs - principaux endpoints

Permet d'interroger les indicateurs de consommation d'espace ainsi que les indicateurs de marché : accessibilité, activité, prix et valorisation.


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
  client.indicateurs.accessibilite(codes_aav="001")
  ```
- Accessibilité pour plusieurs AAV :
  ```python
  client.indicateurs.accessibilite(codes_aav=["004", "005"])
  ```
- Accessibilité pour une année donnée :
  ```python
  client.indicateurs.accessibilite(codes_aav="004", annee="2021")
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
  client.indicateurs.activite(codes="243500139", echelle="epci")
  ```
- Activité pour plusieurs codes :
  ```python
  client.indicateurs.activite(codes=["59001", "59002"], echelle="communes")
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
  client.indicateurs.prix(codes=["59350", "59009"], echelle="communes", ordering="-annee")
  ```

---

## 📂 `indicateurs.valorisation`

### Description

::: apifoncier.endpoints.indicateurs.IndicateurEndpoint.valorisation

### Exemples d'utilisation

- Valorisation pour une AAV :
  ```python
  client.indicateurs.valorisation(code="004", echelle="aav")
  ```
- Valorisation pour un EPCI :
  ```python
  client.indicateurs.valorisation(code="243500139", echelle="epci")
  ```
- Valorisation pour une année donnée :
  ```python
  client.indicateurs.valorisation(code="005", echelle="aav", annee="2021")
  ```
