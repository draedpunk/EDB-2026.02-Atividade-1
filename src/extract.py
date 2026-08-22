import requests

class Extract():
    def __init__(self):
        self.base_url = "https://servicodados.ibge.gov.br/api/v3/agregados"

    def extract_pnadc(self, tabela="4093", periodos="201201-202601",
                       variavel="4099", localidade="N3[26]",
                       classificacao="2[all]"):
        url = (
            f"{self.base_url}/{tabela}/periodos/{periodos}"
            f"/variaveis/{variavel}?localidades={localidade}"
            f"&classificacao={classificacao}"
        )
        response = requests.get(url)
        data = response.json()
        return data