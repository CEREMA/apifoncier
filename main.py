from apifoncier import ApiFoncierClient


def main():
    client = ApiFoncierClient({"base_url": "https://apidf.k8-dev.cerema.fr/"})
    # response = client.request(
    #     "GET", "/dvf_opendata/mutations", params={"code_insee": "59646"}
    # )
    response = client.endpoint._fetch(
        endpoint="/dvf_opendata/geomutations",
        params={"code_insee": "59646"},
        format_output="dict",
        geo=False,
        paginate=True,
    )
    return response


if __name__ == "__main__":
    print(main())
