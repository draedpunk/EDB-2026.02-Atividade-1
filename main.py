from src.extract import Extract
from src.load import Load

extract = Extract()
load = Load()

# Variáveis pedidas no desafio
variaveis = {
    "4099": "taxa_desocupacao",
    "4096": "taxa_participacao",
    "12466": "taxa_informalidade",
}

# Categorias de sexo pedidas no desafio
sexos = {
    "6794": "total",
    "4": "homens",
    "5": "mulheres",
}

# Estados que o grupo precisa extrair (código N3 do IBGE)
# Exemplo: 26 = Pernambuco, 35 = São Paulo, 33 = Rio de Janeiro
estados = {
    "26": "pernambuco",
    "35": "sao_paulo",
}

for cod_estado, nome_estado in estados.items():
    for cod_var, nome_var in variaveis.items():
        for cod_sexo, nome_sexo in sexos.items():
            print(f"Extraindo {nome_var} - {nome_sexo} - {nome_estado}...")

            dados = extract.extract_pnadc(
                variavel=cod_var,
                localidade=f"N3[{cod_estado}]",
                classificacao=f"2[{cod_sexo}]",
            )

            nome_arquivo = f"{nome_estado}_{nome_var}_{nome_sexo}"
            load.load_json(nome_arquivo, dados)

print("Extração concluída!")