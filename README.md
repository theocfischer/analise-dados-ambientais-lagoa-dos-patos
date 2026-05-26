# Análise de Dados Ambientais da Lagoa dos Patos

Estudo de caso técnico baseado em um estágio obrigatório realizado com foco em tratamento, organização e visualização de dados ambientais da **Lagoa dos Patos**, utilizando **Python**, **Jupyter Notebook**, **pandas**, **NumPy**, **Matplotlib** e dados públicos da **FEPAM** e da **ANA/RNQA**.

> **Status do repositório:** documentação técnica reconstruída a partir dos registros do estágio, conversas de acompanhamento, relatório e material usado em apresentação científica.  
> Os notebooks, bases tratadas e gráficos originais não estão integralmente disponíveis nesta versão pública.

---

## Sumário

1. [Visão geral](#1-visão-geral)  
2. [Contexto do estágio](#2-contexto-do-estágio)  
3. [Objetivo do projeto](#3-objetivo-do-projeto)  
4. [Fontes de dados](#4-fontes-de-dados)  
5. [Ferramentas e tecnologias](#5-ferramentas-e-tecnologias)  
6. [Estrutura do projeto](#6-estrutura-do-projeto)  
7. [Pipeline técnico](#7-pipeline-técnico)  
8. [Parâmetros analisados](#8-parâmetros-analisados)  
9. [Análises realizadas](#9-análises-realizadas)  
10. [Resultados exploratórios](#10-resultados-exploratórios)  
11. [Limitações do projeto](#11-limitações-do-projeto)  
12. [Aprendizados](#12-aprendizados)  
13. [Relação com a Mostra Científica](#13-relação-com-a-mostra-científica)  
14. [Possíveis próximos passos](#14-possíveis-próximos-passos)  
15. [Competências demonstradas](#15-competências-demonstradas)  
16. [Aviso sobre reprodutibilidade](#16-aviso-sobre-reprodutibilidade)  

## Documentos complementares

- [Mostra Científica](docs/mostra-cientifica.md)
- [Roteiro de apresentação](docs/roteiro-apresentacao.md)
- [Perguntas e respostas para banca](docs/perguntas-banca.md)

---

## 1. Visão geral

Este repositório documenta um estudo de caso técnico baseado em um estágio obrigatório voltado à análise de dados ambientais da Lagoa dos Patos, no Rio Grande do Sul.

O trabalho teve como ideia central aplicar ferramentas de programação e análise de dados para organizar, tratar e visualizar informações relacionadas à qualidade da água. A análise foi feita em ambiente **Jupyter Notebook**, utilizando **Python** e bibliotecas de manipulação e visualização de dados.

O projeto trabalhou com dados públicos da **FEPAM** e da **ANA/RNQA**, buscando analisar parâmetros físico-químicos como:

- pH;
- oxigênio dissolvido;
- salinidade;
- turbidez;
- transparência da água.

A proposta foi exploratória. Ou seja, o objetivo não era produzir uma conclusão ambiental definitiva, mas sim estruturar um fluxo de análise, testar dados reais, gerar visualizações, levantar hipóteses e comunicar os resultados em relatório e banner científico.

---

## 2. Contexto do estágio

O estágio foi realizado no contexto do curso **Técnico em Informática para Internet**, com foco na aplicação de programação e análise de dados a um problema ambiental real.

O tema escolhido foi a **qualidade da água da Lagoa dos Patos**, um dos principais sistemas lagunares do Rio Grande do Sul. A Lagoa dos Patos possui grande importância ambiental, econômica e social, além de estar conectada a dinâmicas de água doce, influência marinha, chuvas, enchentes e atividades humanas.

O trabalho foi desenvolvido de forma remota, em ambiente doméstico, utilizando computador pessoal e ferramentas de análise de dados.

Durante o processo, foram trabalhados dados públicos, arquivos CSV e XLS, organização de pastas, limpeza de bases, geração de gráficos e preparação de material para apresentação científica.

O período do estágio foi de **11/08/2025 a 17/10/2025**.

---

## 3. Objetivo do projeto

O objetivo geral foi aplicar Python para coletar, tratar, visualizar e interpretar dados ambientais sobre a qualidade da água da Lagoa dos Patos.

Os objetivos específicos foram:

- levantar fontes públicas de dados ambientais;
- baixar e organizar arquivos da FEPAM e da ANA/RNQA;
- ler arquivos CSV e XLS em Python;
- resolver problemas de encoding e formatação;
- filtrar estações de monitoramento relacionadas à Lagoa dos Patos;
- limpar e padronizar colunas;
- organizar os dados em formato adequado para análise;
- calcular estatísticas e médias anuais;
- gerar gráficos de tendência;
- criar matriz de correlação entre parâmetros;
- interpretar os resultados de forma exploratória;
- apoiar a construção de relatório técnico e banner científico.

---

## 4. Fontes de dados

Durante o estágio foram utilizadas ou investigadas bases públicas relacionadas ao monitoramento da qualidade da água.

As principais fontes foram:

- **FEPAM** — Fundação Estadual de Proteção Ambiental do Rio Grande do Sul;
- **ANA** — Agência Nacional de Águas e Saneamento Básico;
- **RNQA** — Rede Nacional de Monitoramento da Qualidade da Água;
- bases de estações de monitoramento;
- bases de medições físico-químicas;
- arquivos CSV;
- arquivos XLS.

Entre os arquivos trabalhados ou mencionados ao longo do projeto estavam:

```text
IQ_OD_2021.csv
Rede_Nacional_de_Monitoramento_da_Qualidade_da_Água_(RNQA)_-_Estações_implantadas_por_ano.csv
FEPAM_estacoes.csv
filtradas_fepam_LP.xls
FEPAM_estacoes_Lagoa.csv
fepam_lagoa_dos_patos_limpo.csv
RNQA_lagoa_patos.csv
```

Um dos desafios do projeto foi entender que nem sempre as bases públicas usam a mesma forma de identificação. Em alguns casos, as estações apareciam com códigos diferentes, nomes diferentes, campos de latitude/longitude, campos de recurso hídrico ou identificadores como `CDHIDRO`.

Por isso, a etapa de seleção das estações foi uma das partes mais importantes do trabalho.

---

## 5. Ferramentas e tecnologias

As principais ferramentas e bibliotecas utilizadas foram:

- **Python**;
- **Jupyter Notebook**;
- **Anaconda / Jupyter Lab**;
- **pandas**;
- **NumPy**;
- **Matplotlib**;
- **Seaborn**;
- leitura de arquivos **CSV**;
- leitura de arquivos **XLS**;
- organização de dados em pastas;
- GitHub para documentação do estudo de caso.

Também foram considerados, para possíveis etapas futuras com mapas:

- GeoPandas;
- Folium;
- Shapely.

---

## 6. Estrutura do projeto

Durante o estágio, a pasta principal foi organizada aproximadamente assim:

```text
Estagio_LagoaDosPatos/
│
├── apresentacao/
├── dados_brutos/
├── dados_tratados/
├── notebooks/
├── relatorio/
├── cleanup_project.ipynb
└── Untitled.ipynb
```

A função de cada pasta era:

- `dados_brutos/`: guardar os arquivos originais baixados da FEPAM, ANA ou RNQA, sem edição manual;
- `dados_tratados/`: guardar versões limpas, filtradas ou padronizadas das bases;
- `notebooks/`: guardar notebooks organizados por etapa de análise;
- `relatorio/`: guardar imagens, tabelas, mapas, gráficos e saídas usadas no relatório ou banner;
- `apresentacao/`: guardar materiais de apresentação;
- `Untitled.ipynb`: notebook usado inicialmente para testes soltos;
- `cleanup_project.ipynb`: notebook relacionado a tentativas de limpeza ou organização.

Uma estrutura mais organizada, planejada para a continuidade do projeto, seria:

```text
Estagio_LagoaDosPatos/
│
├── dados_brutos/
│   └── arquivos originais da FEPAM/ANA
│
├── dados_tratados/
│   └── bases limpas e filtradas
│
├── notebooks/
│   ├── 01_preprocessamento.ipynb
│   ├── 02_analise_exploratoria.ipynb
│   ├── 03_visualizacoes.ipynb
│   └── 04_relatorio_final.ipynb
│
├── relatorio/
│   ├── tabelas/
│   ├── graficos/
│   └── material_para_apresentacao/
│
└── README.md
```

Essa organização foi pensada para evitar bagunça no projeto, facilitar a reprodutibilidade e separar claramente dados originais, dados tratados, códigos e resultados.

---

## 7. Pipeline técnico

O fluxo técnico do projeto pode ser resumido nas etapas abaixo.

---

### 7.1 Organização do ambiente

O trabalho foi desenvolvido em Python, dentro do Jupyter Notebook/Jupyter Lab.

As bibliotecas principais eram importadas no início do notebook:

```python
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

Em uma etapa inicial, foi sugerido testar se as bibliotecas estavam funcionando:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Tudo certo com as libs.")
```

Também foi pensado um ambiente Conda específico para o projeto:

```bash
conda create -n estagio_lagoa python=3.10 -y
conda activate estagio_lagoa
conda install jupyterlab pandas numpy matplotlib seaborn -y
```

Para possíveis mapas, também foi cogitado:

```bash
conda install -c conda-forge geopandas folium shapely -y
```

---

### 7.2 Caminhos do projeto

Uma etapa importante foi definir caminhos para as pastas do projeto, evitando depender de caminhos absolutos do computador.

```python
import os
import pandas as pd
import numpy as np

ROOT = os.path.join(os.getcwd(), "..")
PROJECT_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))

DATA_BRUTOS = os.path.join(PROJECT_DIR, "dados_brutos")
DATA_TRATADOS = os.path.join(PROJECT_DIR, "dados_tratados")
RELATORIO = os.path.join(PROJECT_DIR, "relatorio")

print("PROJECT_DIR:", PROJECT_DIR)
print("dados_brutos:", DATA_BRUTOS)
print("dados_tratados:", DATA_TRATADOS)
```

Para listar os arquivos disponíveis na pasta de dados brutos:

```python
for f in os.listdir(DATA_BRUTOS):
    print(f)
```

Essa etapa era importante para verificar se o Jupyter estava rodando na pasta certa e se os arquivos estavam realmente acessíveis.

---

### 7.3 Leitura inicial dos CSVs

Os dois primeiros arquivos principais eram:

```text
IQ_OD_2021.csv
Rede_Nacional_de_Monitoramento_da_Qualidade_da_Água_(RNQA)_-_Estações_implantadas_por_ano.csv
```

A leitura inicial foi feita com `pandas`:

```python
f1 = os.path.join(DATA_BRUTOS, "IQ_OD_2021.csv")

f2 = [
    fn for fn in os.listdir(DATA_BRUTOS)
    if fn.startswith("Rede_Nacional_de_Monitoramento")
][0]

f2 = os.path.join(DATA_BRUTOS, f2)

df_iq = pd.read_csv(f1, encoding="utf-8", low_memory=False)
df_rnqa = pd.read_csv(f2, encoding="utf-8", low_memory=False)

print("IQ_OD head:")
display(df_iq.head())
print("IQ_OD shape:", df_iq.shape)

print("\nRNQA head:")
display(df_rnqa.head())
print("RNQA shape:", df_rnqa.shape)
```

Quando apareciam erros de encoding, a alternativa era tentar:

```python
df_iq = pd.read_csv(f1, encoding="latin1", low_memory=False)
df_rnqa = pd.read_csv(f2, encoding="latin1", low_memory=False)
```

Depois da leitura, a inspeção das colunas era feita com:

```python
print("IQ_OD columns:", list(df_iq.columns))
print("\nRNQA columns:", list(df_rnqa.columns))
```

---

### 7.4 Filtro por Rio Grande do Sul e problema com `sguf`

Em uma das etapas, foi percebido que uma base tinha a coluna `sguf`, mas a outra não.

A seleção inicial tinha algo parecido com:

```python
df_iq_sel: ['objectid', 'cd', 'sguf', 'entidade', 'ambiente', 'latitude', 'longitude']
df_rnqa_sel: ['objectid', 'cdest', 'nmest', 'cdhidro', 'latitude', 'longitude']
```

O erro surgiu porque foi tentado filtrar `df_rnqa_sel` por `sguf`, mas essa coluna não existia nele.

A solução foi checar antes se a coluna existia:

```python
print("Colunas em df_iq_sel:", df_iq_sel.columns.tolist())
print("Colunas em df_rnqa_sel:", df_rnqa_sel.columns.tolist())

if "sguf" in df_iq_sel.columns:
    df_iq_rs = df_iq_sel[df_iq_sel["sguf"].str.upper() == "RS"].copy()
else:
    print("df_iq_sel não tem coluna 'sguf'; usando tudo.")
    df_iq_rs = df_iq_sel.copy()

if "sguf" in df_rnqa_sel.columns:
    df_rnqa_rs = df_rnqa_sel[df_rnqa_sel["sguf"].str.upper() == "RS"].copy()
else:
    print("df_rnqa_sel não tem coluna 'sguf'; mantendo todas as linhas.")
    df_rnqa_rs = df_rnqa_sel.copy()

print(f"Estações IQA do RS: {df_iq_rs.shape[0]}")
print(f"Estações RNQA sem filtro SGUF: {df_rnqa_rs.shape[0]}")
```

Esse tipo de problema mostrou uma dificuldade comum em dados reais: nem sempre as bases usam as mesmas colunas, nomes ou padrões.

---

### 7.5 Filtro geográfico da Lagoa dos Patos

Uma das estratégias testadas foi filtrar estações por latitude e longitude, criando uma caixa geográfica aproximada para a região da Lagoa dos Patos.

```python
df_rnqa_rs["latitude"] = pd.to_numeric(df_rnqa_rs["latitude"], errors="coerce")
df_rnqa_rs["longitude"] = pd.to_numeric(df_rnqa_rs["longitude"], errors="coerce")

min_lat, max_lat = -33.5, -30.0
min_lon, max_lon = -52.5, -50.0

df_rnqa_lagoa = df_rnqa_rs[
    (df_rnqa_rs["latitude"].between(min_lat, max_lat)) &
    (df_rnqa_rs["longitude"].between(min_lon, max_lon))
].copy()

print(f"Estações RNQA na região da Lagoa dos Patos: {df_rnqa_lagoa.shape[0]}")
display(df_rnqa_lagoa.head())

df_rnqa_lagoa.to_csv(
    os.path.join(DATA_TRATADOS, "RNQA_lagoa_patos.csv"),
    index=False
)
```

A lógica dessa etapa era:

1. converter latitude e longitude para número;
2. definir limites aproximados da região;
3. filtrar estações dentro da área;
4. salvar a tabela filtrada.

Essa estratégia era útil para um recorte amplo, mas também tinha limitações, porque uma estação próxima geograficamente nem sempre representa diretamente a Lagoa dos Patos.

---

### 7.6 Entrada dos dados da FEPAM

Depois, o foco mudou para dados da FEPAM, especialmente uma planilha chamada:

```text
filtradas_fepam_LP.xls
```

A leitura da planilha foi pensada assim:

```python
import pandas as pd
import os

fepam_xls_path = os.path.join(DATA_BRUTOS, "filtradas_fepam_LP.xls")

xls = pd.ExcelFile(fepam_xls_path)
print("Abas encontradas:", xls.sheet_names)

df_med = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

print("Planilha lida com sucesso!")
print("Shape:", df_med.shape)
print("Colunas:")
print(list(df_med.columns))

display(df_med.head(10))
```

Durante essa etapa, apareceu um erro relacionado ao pacote `xlrd`.

O erro indicava que o pandas precisava da dependência `xlrd` para ler arquivos `.xls`:

```text
ModuleNotFoundError: No module named 'xlrd'
ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 2.0.1 for xls Excel support
```

A solução seria instalar o pacote:

```bash
pip install xlrd
```

ou, em ambiente Conda:

```bash
conda install xlrd
```

---

### 7.7 Problemas de encoding nos dados da FEPAM

Alguns textos apareceram com caracteres quebrados, como:

```text
SÃ£o
GonÃ§alo
MunicÃ­pio
```

Esse tipo de problema é comum quando o arquivo foi salvo em uma codificação e lido em outra.

Uma tentativa de leitura foi:

```python
df_fepam = pd.read_csv(fepam_path, sep=",", encoding="latin1")
```

Depois, foi feita limpeza de nomes de colunas:

```python
df_fepam.columns = (
    df_fepam.columns
    .str.strip()
    .str.replace("Ã§", "ç")
    .str.replace("Ã£", "ã")
    .str.replace("Ã¡", "á")
    .str.replace("Ãª", "ê")
    .str.replace("Ã³", "ó")
    .str.replace("Ã", "A")
    .str.replace("¢", "ç")
)

print("Colunas limpas:")
print(list(df_fepam.columns))
display(df_fepam.head(10))
```

Também foi usada uma função para tentar corrigir valores internos:

```python
import unicodedata

def corrigir_texto(texto):
    """Tenta corrigir caracteres estranhos vindos de encoding errado."""
    if isinstance(texto, str):
        try:
            texto = texto.encode("latin1").decode("utf-8")
        except:
            pass
        texto = unicodedata.normalize("NFKC", texto)
    return texto

df_fepam.columns = [corrigir_texto(c) for c in df_fepam.columns]

for col in df_fepam.select_dtypes(include=["object"]).columns:
    df_fepam[col] = df_fepam[col].map(corrigir_texto)

print("Colunas e textos corrigidos com sucesso!")
print(list(df_fepam.columns))
display(df_fepam.head(10))
```

Essa etapa foi importante porque nomes de colunas e valores textuais quebrados dificultam filtros, buscas e interpretação.

---

### 7.8 Filtro por `Recurso Hídrico`

Em uma das bases da FEPAM, a coluna correta para identificar o corpo hídrico era:

```text
Recurso Hídrico
```

Foi feito um filtro por estações associadas à Lagoa dos Patos:

```python
import pandas as pd

df = pd.read_csv("../dados_brutos/FEPAM_estacoes.csv", encoding="utf-8")

df_lagoa = df[
    df["Recurso Hídrico"].str.contains("Lagoa dos Patos", case=False, na=False)
]

print(
    f"Encontradas {df_lagoa.shape[0]} estações com "
    "'Lagoa dos Patos' como Recurso Hídrico:"
)

display(df_lagoa[
    [
        "Cód. Estção de Monitoramento",
        "Recurso Hídrico",
        "Município",
        "Tipo",
        "Latitude",
        "Longitude"
    ]
])

df_lagoa.to_csv("../dados_tratados/FEPAM_estacoes_Lagoa.csv", index=False)
```

O resultado esperado era encontrar apenas **duas estações** com `Lagoa dos Patos` diretamente cadastrada como recurso hídrico.

Esse recorte foi usado por ser mais objetivo, mas também foi reconhecido como limitação metodológica. Muitas estações próximas ou relacionadas ao sistema lagunar podem estar cadastradas com outros nomes, como Canal de Rio Grande, Lagoa Mirim, São Gonçalo ou outros corpos hídricos associados.

---

### 7.9 Limpeza inicial das medições da FEPAM

Depois da leitura da planilha de medições, foram selecionadas colunas de interesse:

```python
colunas_interesse = [
    "Data Coleta",
    "Latitude",
    "Longitude",
    "pH",
    "Oxigênio Dissolvido (mg/L)",
    "Salinidade (ppt)",
    "Turbidez (UNT)",
    "Transparência da Água (m)"
]
```

Em seguida, as colunas foram padronizadas para nomes mais simples:

```python
df_med = df_med[colunas_interesse].copy()

df_med.columns = [
    "data",
    "latitude",
    "longitude",
    "ph",
    "oxigenio_dissolvido",
    "salinidade",
    "turbidez",
    "transparencia"
]
```

Depois, foi feita conversão da coluna de data e remoção de registros incompletos:

```python
df_med["data"] = pd.to_datetime(df_med["data"], errors="coerce")

df_med = df_med.dropna(subset=["data"])

df_med = df_med.dropna(
    subset=[
        "ph",
        "oxigenio_dissolvido",
        "salinidade",
        "turbidez",
        "transparencia"
    ],
    how="all"
)

print("Dados limpos e formatados!")
print("Shape final:", df_med.shape)
display(df_med.head(10))
```

A base limpa poderia ser salva em uma pasta de dados processados:

```python
df_med.to_csv(
    "../dados_processados/fepam_lagoa_dos_patos_limpo.csv",
    index=False
)
```

---

## 8. Parâmetros analisados

### 8.1 pH

O pH indica se a água é ácida, neutra ou alcalina.

- pH abaixo de 7: ácido;
- pH igual a 7: neutro;
- pH acima de 7: alcalino ou básico.

Em águas naturais, valores geralmente ficam em torno de 6 a 9. Mudanças bruscas podem indicar alterações químicas, poluição ou influência de água marinha.

No projeto, o pH foi analisado como um indicador geral das condições químicas da água.

---

### 8.2 Oxigênio dissolvido

O oxigênio dissolvido, ou OD, representa a quantidade de oxigênio disponível na água.

Esse parâmetro é essencial para peixes e outros organismos aquáticos, porque eles dependem desse oxigênio para respirar.

Valores muito baixos de OD podem indicar:

- excesso de matéria orgânica;
- poluição;
- baixa circulação da água;
- degradação da qualidade ambiental;
- condições desfavoráveis à vida aquática.

No estudo, o OD foi usado como um dos principais indicadores de qualidade da água.

---

### 8.3 Salinidade

A salinidade mede a quantidade de sais dissolvidos na água.

A Lagoa dos Patos é um ambiente lagunar/estuarino, com influência tanto de água doce quanto de água salgada. A salinidade pode variar conforme:

- entrada de água doce pelos rios;
- influência do oceano;
- períodos de chuva;
- períodos secos;
- ventos e circulação da água;
- enchentes.

No projeto, a salinidade foi importante para observar possíveis mudanças na dinâmica entre água doce e influência marinha.

---

### 8.4 Turbidez

A turbidez indica o quanto a água está turva, geralmente por causa de partículas em suspensão.

Essas partículas podem ser:

- sedimentos;
- argila;
- matéria orgânica;
- algas;
- material carregado por chuvas e enchentes.

A turbidez pode aumentar em situações como:

- chuvas fortes;
- erosão;
- ressuspensão de sedimentos;
- enchentes;
- entrada de material orgânico no corpo d’água.

No projeto, a turbidez foi um dos parâmetros que apresentou maior variação, especialmente em 2024.

---

### 8.5 Transparência

A transparência indica a profundidade até onde é possível enxergar através da água.

Ela está relacionada à turbidez: em geral, quanto mais turva a água, menor tende a ser a transparência.

A transparência foi considerada em parte das análises, mas posteriormente foi removida de algumas visualizações, como a matriz de correlação, para facilitar a leitura dos resultados.

---

## 9. Análises realizadas

### 9.1 Verificação de estatísticas básicas

Uma das primeiras análises foi verificar estatísticas descritivas dos dados.

```python
df_med.describe()
```

Essa etapa ajuda a observar:

- quantidade de registros;
- média;
- desvio padrão;
- valores mínimos;
- valores máximos;
- possíveis valores anômalos.

---

### 9.2 Verificação de valores fora do esperado

Também foi criada uma verificação simples de faixas plausíveis para alguns parâmetros.

```python
limites = {
    "ph": (6, 9),
    "oxigenio_dissolvido": (0, 15),
    "salinidade": (0, 35),
    "turbidez": (0, 150),
    "transparencia": (0, 5)
}

for param, (min_v, max_v) in limites.items():
    fora = df_med[(df_med[param] < min_v) | (df_med[param] > max_v)]

    print(
        f"{param.upper()} -> {len(fora)} valores fora "
        f"do intervalo esperado ({min_v}–{max_v})"
    )

    if not fora.empty:
        print(fora[["data", param]])
```

Esses limites não servem como diagnóstico final, mas ajudam a encontrar valores estranhos que merecem revisão.

---

### 9.3 Médias anuais

Foi criada uma análise de médias anuais para observar variações dos parâmetros ao longo dos anos.

```python
df_med["ano"] = df_med["data"].dt.year

media_anual = df_med.groupby("ano")[
    [
        "ph",
        "oxigenio_dissolvido",
        "salinidade",
        "turbidez",
        "transparencia"
    ]
].mean()

print("Médias anuais calculadas:")
display(media_anual)
```

Essa etapa foi usada para gerar gráficos de tendência e observar se os parâmetros variavam muito de um ano para outro.

---

### 9.4 Gráficos individuais de tendência anual

Uma versão dos gráficos foi feita com um gráfico separado para cada parâmetro:

```python
fig, axs = plt.subplots(5, 1, figsize=(8, 18))

for i, col in enumerate(media_anual.columns):
    axs[i].plot(media_anual.index, media_anual[col], marker="o")
    axs[i].set_title(f"Tendência Anual — {col.capitalize()}")
    axs[i].set_xlabel("Ano")
    axs[i].set_ylabel(col.capitalize())
    axs[i].grid(True)

plt.tight_layout()
plt.show()
```

Esse formato facilita a leitura porque cada parâmetro pode ter unidade e escala própria.

---

### 9.5 Gráfico único com todos os parâmetros

Também foi testado um gráfico único com todos os parâmetros juntos:

```python
import matplotlib.pyplot as plt
import pandas as pd

df_med["ano"] = pd.to_datetime(df_med["data"]).dt.year

media_anual = df_med.groupby("ano")[
    [
        "ph",
        "oxigenio_dissolvido",
        "salinidade",
        "turbidez",
        "transparencia"
    ]
].mean()

plt.figure(figsize=(10, 6))

for col in media_anual.columns:
    plt.plot(
        media_anual.index,
        media_anual[col],
        label=col.capitalize(),
        linewidth=2
    )

plt.title("Tendência Anual dos Parâmetros de Qualidade da Água - Lagoa dos Patos")
plt.xlabel("Ano")
plt.ylabel("Média Anual")
plt.legend(title="Parâmetros", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
```

Esse gráfico é visualmente interessante, mas possui uma limitação: os parâmetros não têm todos a mesma unidade. Por isso, valores de turbidez, pH, salinidade e oxigênio dissolvido podem ficar difíceis de comparar diretamente no mesmo eixo.

---

### 9.6 Matriz de correlação

Foi criada uma matriz de correlação para observar relações estatísticas entre os parâmetros.

```python
corr = df_med[
    [
        "ph",
        "oxigenio_dissolvido",
        "salinidade",
        "turbidez",
        "transparencia"
    ]
].corr()

print("Matriz de Correlação:")
display(corr)

plt.figure(figsize=(6, 5))
plt.imshow(corr, cmap="coolwarm", interpolation="none")
plt.colorbar(label="Coeficiente de Correlação (r)")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Matriz de Correlação entre Parâmetros")
plt.tight_layout()
plt.show()
```

Depois, a transparência foi removida para deixar a visualização mais clara:

```python
corr = df_med[
    [
        "ph",
        "oxigenio_dissolvido",
        "salinidade",
        "turbidez"
    ]
].corr()
```

A correlação foi usada como ferramenta exploratória. Ela ajuda a observar se duas variáveis tendem a variar juntas, mas não prova causa.

Interpretação geral:

- próximo de `+1`: as variáveis tendem a subir juntas;
- próximo de `-1`: quando uma sobe, a outra tende a cair;
- próximo de `0`: não há relação linear clara.

---

### 9.7 Verificação de coerência dos dados

Durante a análise, foi discutido se os valores encontrados pareciam coerentes.

De modo geral, foram considerados plausíveis:

- pH em torno de 7,4 a 8,6;
- oxigênio dissolvido entre 5 e 12 mg/L;
- salinidade entre 0 e 30 ppt;
- turbidez com possibilidade de passar de 200 UNT em eventos extremos;
- transparência entre 0,1 e 2 metros.

Picos e variações bruscas poderiam ocorrer por fatores como:

- sazonalidade;
- chuvas intensas;
- enchentes;
- intrusão marinha;
- ressuspensão de sedimentos;
- lacunas ou falhas de amostragem;
- diferenças entre estações.

---

## 10. Resultados exploratórios

A análise permitiu levantar algumas observações iniciais.

Os dados indicaram comportamento compatível com um ambiente lagunar/estuarino, com variações entre os anos e diferenças entre parâmetros.

Entre os principais resultados exploratórios:

- o pH se manteve em uma faixa levemente alcalina;
- o oxigênio dissolvido variou dentro de faixas consideradas plausíveis;
- a salinidade apresentou variações relevantes entre os anos;
- a turbidez apresentou oscilações fortes e pico expressivo em 2024;
- a transparência apresentou comportamento relacionado à turbidez;
- a matriz de correlação ajudou a observar relações entre os parâmetros;
- os resultados sugerem influência de fatores sazonais, regime de chuvas, entrada de água do mar e eventos extremos.

Um ponto discutido foi a possibilidade de as alterações em 2024 estarem relacionadas às enchentes históricas no Rio Grande do Sul. Essa hipótese faz sentido como possibilidade, já que enchentes podem aumentar o transporte de sedimentos, alterar a salinidade, carregar matéria orgânica e modificar temporariamente as condições da água.

Mesmo assim, as conclusões devem ser tratadas com cuidado. O estudo foi exploratório e dependia da qualidade das bases, da escolha das estações e da continuidade da análise.

---

## 11. Limitações do projeto

O projeto apresentou limitações importantes:

- os notebooks originais não estão integralmente disponíveis nesta versão pública;
- os gráficos originais não foram incluídos neste repositório;
- as bases tratadas não foram publicadas aqui;
- algumas imagens e anexos do processo original não puderam ser recuperados;
- a extração textual da conversa não trouxe todos os prints e resultados visuais;
- a base da FEPAM retornou apenas duas estações diretamente associadas à Lagoa dos Patos pelo campo `Recurso Hídrico`;
- muitas estações próximas podem estar cadastradas com outros nomes de recurso hídrico;
- houve diferenças entre bases da FEPAM e da ANA/RNQA;
- alguns arquivos apresentaram problemas de encoding;
- parâmetros diferentes possuem unidades diferentes, dificultando comparação direta em um único gráfico;
- faltaram variáveis biológicas, como nutrientes, algas e coliformes;
- a análise não substitui um estudo ambiental completo.

Por isso, este repositório deve ser entendido como documentação técnica e estudo de caso do processo desenvolvido, não como reprodução integral do ambiente original do estágio.

---

## 12. Aprendizados

O estágio ajudou a desenvolver habilidades técnicas e profissionais ligadas a dados, programação e comunicação científica.

Entre os principais aprendizados:

- organizar um projeto de dados em pastas;
- trabalhar com dados brutos sem editá-los manualmente;
- ler arquivos CSV e XLS com pandas;
- resolver problemas de encoding;
- lidar com arquivos que exigem dependências externas, como `xlrd`;
- inspecionar colunas e tipos de dados;
- filtrar dados por atributos, códigos, coordenadas e recurso hídrico;
- limpar e padronizar colunas;
- trabalhar com datas;
- calcular médias anuais;
- gerar gráficos com Matplotlib;
- interpretar uma matriz de correlação;
- entender limitações de dados públicos;
- documentar processos técnicos;
- transformar resultados em relatório e banner científico.

A experiência também mostrou que trabalhar com dados reais é diferente de trabalhar com exemplos prontos. Em dados reais, grande parte do esforço está em entender a base, corrigir problemas, validar se os valores fazem sentido e tomar decisões metodológicas.

---

## 13. Relação com a Mostra Científica

Os resultados do estágio foram organizados para apresentação em formato de banner científico na Mostra Científica.

A apresentação abordou:

- análise da qualidade da água da Lagoa dos Patos entre 2017 e 2024;
- uso de dados públicos da FEPAM;
- filtragem de estações ligadas à Lagoa dos Patos;
- tratamento dos dados em Jupyter Notebook;
- uso de Python, pandas e Matplotlib;
- cálculo de médias anuais;
- gráficos de tendência;
- matriz de correlação;
- interpretação de parâmetros como pH, oxigênio dissolvido, salinidade e turbidez.

A metodologia apresentada no banner pode ser resumida assim:

> O trabalho utilizou bases públicas de monitoramento da qualidade da água disponibilizadas pela FEPAM/RS, focando nas estações localizadas na Lagoa dos Patos. Os dados foram tratados e analisados em ambiente Jupyter Notebook, com programação em Python e uso das bibliotecas pandas e Matplotlib. As principais etapas foram limpeza, padronização, cálculo de estatísticas descritivas, análise temporal das variações anuais e correlações entre parâmetros físico-químicos.

Os resultados foram apresentados como uma análise inicial. Os parâmetros com maior variação foram turbidez e salinidade, com alterações fortes em 2024 possivelmente relacionadas às enchentes. pH e oxigênio dissolvido ficaram dentro de faixas consideradas plausíveis, e a matriz de correlação ajudou a observar relações entre variáveis.

A conclusão geral foi que dados públicos e programação podem ajudar a entender melhor a qualidade da água da Lagoa dos Patos, servindo como base para estudos futuros mais completos.

---

## 14. Possíveis próximos passos

Este projeto pode ser expandido futuramente com:

- recuperação dos notebooks originais;
- recuperação dos gráficos utilizados no banner;
- inclusão de bases públicas em versão reproduzível;
- recriação de uma análise demonstrativa com dados públicos;
- organização de notebooks por etapa;
- comparação entre mais estações;
- integração com novas bases da ANA/RNQA;
- análise sazonal;
- investigação mais detalhada das enchentes de 2024;
- inclusão de dados de chuva, vazão ou clima;
- criação de mapas das estações;
- visualizações interativas;
- relatório técnico complementar;
- documentação mais completa do processo.

Uma versão futura ideal poderia ter esta estrutura:

```text
analise-dados-ambientais-lagoa-dos-patos/
│
├── dados_exemplo/
│   └── amostra_publica.csv
│
├── notebooks/
│   ├── 01_preprocessamento.ipynb
│   ├── 02_analise_exploratoria.ipynb
│   └── 03_visualizacoes.ipynb
│
├── imagens/
│   ├── tendencias_anuais.png
│   └── matriz_correlacao.png
│
├── docs/
│   └── relatorio_tecnico.md
│
└── README.md
```

---

## 15. Competências demonstradas

Este estudo de caso demonstra conhecimentos e práticas relacionados a:

- Python;
- pandas;
- NumPy;
- Matplotlib;
- Seaborn;
- Jupyter Notebook;
- Anaconda;
- análise de dados;
- tratamento de dados;
- dados ambientais;
- dados públicos;
- leitura de CSV;
- leitura de XLS;
- limpeza de dados;
- padronização de colunas;
- manipulação de datas;
- cálculo de médias anuais;
- visualização de dados;
- análise de correlação;
- documentação técnica;
- comunicação científica;
- organização de projeto;
- uso de GitHub como portfólio.

---

## 16. Aviso sobre reprodutibilidade

Esta versão do repositório tem caráter documental.

Os dados, notebooks e gráficos originais do estágio não estão integralmente disponíveis nesta publicação. Parte do conteúdo foi reconstruída a partir de registros do processo, relatório, material de apresentação e anotações técnicas.

Por esse motivo, o repositório não deve ser interpretado como uma reprodução completa do ambiente original de análise, mas sim como um estudo de caso técnico que registra o processo desenvolvido, as ferramentas utilizadas, os desafios encontrados e os aprendizados obtidos.

Uma versão futura poderá incluir notebooks e bases públicas para permitir reprodução completa da análise.

---

## Referências e fontes relacionadas

- FEPAM — Fundação Estadual de Proteção Ambiental do Rio Grande do Sul  
  https://www.fepam.rs.gov.br

- ANA — Agência Nacional de Águas e Saneamento Básico  
  https://www.gov.br/ana

- Python Software Foundation — Python Documentation  
  https://docs.python.org/3/

- pandas — Python Data Analysis Library  
  https://pandas.pydata.org/

- Matplotlib — Visualization with Python  
  https://matplotlib.org/

- Jupyter Project  
  https://jupyter.org/
