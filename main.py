from apifoncier import ApiFoncierClient

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3NTIzMDk4LCJpYXQiOjE3NTQ5MzEwOTgsImp0aSI6IjJhOGY2MzQxMmIzNDQ3MWFiODU1NDAzMDU3MGZlMTBiIiwidXNlcl9uYW1lIjoiYW50b2luZS5oZXJtYW4iLCJhdWQiOiJhcGlkZiJ9.HpGcCaJ4CodRUrxakfhtTmw-SiOsh7-S8QlDecICUg8"


def friche_sample():
    with ApiFoncierClient({"base_url": "https://apidf.k8-dev.cerema.fr/"}) as apidf:
        df_friches = apidf.cartofriches.geofriches(
            codes_insee=["59646", "59650"],
            # lon_lat=[2.7, 49.7],
            # in_bbox=[2.76, 49.73, 2.779, 49.749],
            # contains_lon_lat=[3.065239, 50.625278],
            format_output="dataframe",
            paginate=True,
            page_size=500,
        )
        print(f"Nombre de friches récupérées : {len(df_friches)}")
        print(df_friches.head())

        return df_friches


def mutation_sample():

    with ApiFoncierClient(
        {"api_key": API_KEY, "base_url": "https://apidf-preprod.cerema.fr/"}
    ) as client:

        # DVF+ (accès libre)
        # df = client.dvf_opendata.mutations(
        #     code_insee="59646", anneemut_min="2023", codtypbien="11,12", paginate=True
        # )

        # DV3F (accès restreint)
        df = client.dv3f.mutations(
            code_insee="59350",
            anneemut_min="2020",
            codtypproa="X",  # Acheteur particulier
            codtypprov="X",  # Vendeur particulier
            sbati_min=50.0,
            codtypbien="11,12",  # Logements
            paginate=True,
        )

        # Mutations géolocalisées DVF+
        # gdf_geo = client.dvf_opendata.geomutations(
        #     in_bbox=[2.76, 49.73, 2.779, 49.749], anneemut="2023", paginate=True
        # )

        # Mutation spécifique par ID
        # mutation_detail = client.dvf_opendata.mutation_by_id(12345)

        print(f"DVF+ mutations: {len(df)}")
        print(df.head())

        return df
        # print(f"DV3F mutations: {len(df_dv3f)}")
        # print(f"Géomutations: {len(gdf_geo)}")
        # print(gdf_geo.head())


def parcelle_sample():

    with ApiFoncierClient(
        {"api_key": API_KEY, "base_url": "https://apidf-preprod.cerema.fr/"}
    ) as client:

        # DVF+ (accès libre)
        # df = client.dvf_opendata.mutations(
        #     code_insee="59646", anneemut_min="2023", codtypbien="11,12", paginate=True
        # )

        # DV3F (accès restreint)
        df = client.ff.geoparcelles(
            code_insee="59646",
            catpro3="P",
            paginate=True,
            dcntpa_min="300",
        )

        # Mutations géolocalisées DVF+
        # gdf_geo = client.dvf_opendata.geomutations(
        #     in_bbox=[2.76, 49.73, 2.779, 49.749], anneemut="2023", paginate=True
        # )

        # Mutation spécifique par ID
        # mutation_detail = client.dvf_opendata.mutation_by_id(12345)

        print(f"FF mutations: {len(df)}")
        print(df.head())

        return df
        # print(f"DV3F mutations: {len(df_dv3f)}")
        # print(f"Géomutations: {len(gdf_geo)}")
        # print(gdf_geo.head())


if __name__ == "__main__":
    df = parcelle_sample()
    print(df.dcntpa.min())
