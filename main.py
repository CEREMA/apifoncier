from apifoncier import ApiFoncierClient


def friche_sample():
    with ApiFoncierClient({"base_url": "https://apidf.k8-dev.cerema.fr/"}) as apidf:
        response = apidf.cartofriches.geofriches(
            codes_insee=["59646", "59650"],
            # lon_lat=[2.7, 49.7],
            # in_bbox=[2.76, 49.73, 2.779, 49.749],
            # contains_lon_lat=[3.065239, 50.625278],
            format_output="dataframe",
            paginate=True,
            page_size=500,
        )
        return response


if __name__ == "__main__":
    print(friche_sample())
