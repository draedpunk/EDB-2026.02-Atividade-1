# Extrator de Dados IBGE - PNAD Contínua (Tabela 4093)

Projeto da disciplina de Engenharia de Dados e Big Data, desenvolvido com Programação Orientada a Objetos (POO), que extrai dados da API pública do IBGE (Tabela 4093 - PNAD Contínua) referentes a taxa de desocupação, taxa de participação na força de trabalho e taxa de informalidade, por estado e sexo.

## Pré-requisitos

- Python 3.10 ou superior instalado
- Git instalado

## Passo a passo para rodar o projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-da-pasta>
```

### 2. Criar o ambiente virtual (venv)

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Windows (cmd):**
```bash
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

> Quando a venv estiver ativa, o terminal mostrará `(venv)` no início da linha.

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o projeto

```bash
python main.py
```

O script irá consultar a API do IBGE e gerar arquivos `.json` na raiz do projeto, um para cada combinação de estado, variável e sexo.

## Variáveis extraídas

| Código | Variável                          |
|--------|------------------------------------|
| 4099   | Taxa de desocupação                |
| 4096   | Taxa de participação na força de trabalho |
| 12466  | Taxa de informalidade              |

## Categorias de sexo

| Código | Categoria |
|--------|-----------|
| 6794   | Total     |
| 4      | Homens    |
| 5      | Mulheres  |

## Estados extraídos

| Código | Estado         |
|--------|----------------|
| 26     | Pernambuco     |
| 35     | São Paulo      |

## Autores

- Diego David Alves Xavier
- Hyngrid Souza e Silva
- Pamela Teixeira Rodrigues 