# DV3F - principaux endpoints

Permet d'interroger les mutations DV3F et leurs géométries.

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
- Mutations DV3F filtrées par année :
  ```python
  client.dv3f.mutations(code_insee="59001", anneemut="2022")
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
  client.dv3f.geomutations(code_insee="59001", codtypbien="MAISON")
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
