# Estudo de Caso — Análise de Dados Ambientais da Lagoa dos Patos

## 1. Sobre o projeto

Este repositório documenta um estudo de caso técnico baseado na minha experiência de estágio obrigatório, realizado entre agosto e outubro de 2025, com foco em análise de dados ambientais da Lagoa dos Patos.

O estágio teve como objetivo utilizar ferramentas de programação e análise de dados para organizar, tratar e visualizar informações relacionadas à qualidade da água, utilizando dados públicos de instituições como FEPAM e ANA.

Esta versão pública não contém todos os notebooks, gráficos e arquivos originais do estágio. O objetivo deste repositório é registrar a metodologia, as ferramentas utilizadas, os desafios encontrados e os aprendizados obtidos durante o processo.

---

## 2. Contexto

A Lagoa dos Patos é um dos principais sistemas lagunares do Rio Grande do Sul e possui grande importância ambiental, econômica e social.

Durante o estágio, o foco foi estudar parâmetros de qualidade da água a partir de bases públicas, buscando compreender variações ao longo do tempo e possíveis relações entre diferentes indicadores ambientais.

O projeto teve caráter exploratório, ou seja, não teve a intenção de produzir conclusões definitivas, mas sim organizar dados, gerar visualizações e levantar hipóteses para análises futuras.

---

## 3. Objetivos

Os principais objetivos do estágio foram:

- utilizar Python para leitura e tratamento de dados ambientais;
- trabalhar com bases públicas da FEPAM e da ANA;
- organizar dados em ambiente Jupyter Notebook;
- filtrar informações relacionadas à Lagoa dos Patos;
- analisar parâmetros físico-químicos da água;
- gerar gráficos e visualizações;
- calcular médias anuais dos parâmetros analisados;
- construir matriz de correlação entre variáveis;
- documentar o processo de análise.

---

## 4. Fontes de dados

Durante o estágio, foram utilizadas ou investigadas bases públicas relacionadas ao monitoramento da qualidade da água.

As principais fontes foram:

- FEPAM — Fundação Estadual de Proteção Ambiental do Rio Grande do Sul;
- ANA — Agência Nacional de Águas e Saneamento Básico;
- bases com informações de estações de monitoramento;
- arquivos em formatos como CSV e XLS;
- dados de parâmetros ambientais, como pH, oxigênio dissolvido, salinidade, turbidez e transparência.

Um dos desafios encontrados foi identificar corretamente quais estações de monitoramento estavam associadas à Lagoa dos Patos, especialmente por causa de diferenças entre códigos, coordenadas e classificações das bases.

---

## 5. Ferramentas utilizadas

As principais ferramentas e bibliotecas utilizadas foram:

- Python;
- Jupyter Notebook;
- pandas;
- NumPy;
- Matplotlib;
- Seaborn;
- Anaconda;
- arquivos CSV e XLS.

O ambiente Jupyter Notebook foi utilizado por permitir escrever código, testar etapas, visualizar resultados e documentar o raciocínio no mesmo local.

---

## 6. Parâmetros analisados

Os principais parâmetros ambientais analisados foram:

### pH

Indica o nível de acidez ou alcalinidade da água. É um parâmetro importante porque alterações muito grandes podem afetar organismos aquáticos e indicar mudanças nas condições ambientais.

### Oxigênio dissolvido

Representa a quantidade de oxigênio disponível na água. É essencial para peixes e outros organismos aquáticos. Baixos níveis de oxigênio dissolvido podem indicar poluição, excesso de matéria orgânica ou condições ambientais desfavoráveis.

### Salinidade

Indica a quantidade de sais dissolvidos na água. Na Lagoa dos Patos, esse parâmetro pode variar devido à influência da água doce dos rios e da entrada de água salgada pelo sul, próxima ao oceano.

### Turbidez

Indica o quanto a água está turva, geralmente por presença de sedimentos, partículas em suspensão ou matéria orgânica. Pode aumentar em períodos de chuva intensa, vento, ressuspensão de sedimentos ou eventos extremos.

### Transparência

Indica a profundidade até onde é possível visualizar através da água. Durante a análise, esse parâmetro foi considerado, mas posteriormente foi deixado de lado em algumas visualizações para facilitar a interpretação dos dados.

---

## 7. Etapas realizadas

O processo de análise envolveu as seguintes etapas:

### 7.1 Coleta e inspeção dos dados

Foram baixados arquivos públicos relacionados ao monitoramento da qualidade da água. Em seguida, os dados foram carregados no Jupyter Notebook para inspeção inicial.

Nessa etapa, foram analisadas colunas, formatos, tipos de dados e possíveis problemas de leitura.

### 7.2 Tratamento de problemas de encoding

Alguns arquivos apresentaram problemas de acentuação e caracteres especiais. Para resolver isso, foram testadas alternativas de leitura, incluindo o uso de encoding como `latin1`.

Esse foi um dos primeiros desafios técnicos do projeto.

### 7.3 Filtragem de estações

Uma etapa importante foi tentar identificar estações de monitoramento associadas à Lagoa dos Patos.

Foram analisadas informações como códigos de estação, nomes, coordenadas, recurso hídrico e identificadores como CDHIDRO.

Esse processo foi necessário porque nem todas as bases apresentavam as estações de forma padronizada.

### 7.4 Organização dos parâmetros

Após a filtragem dos dados, os parâmetros ambientais foram organizados para permitir análise temporal e comparação entre variáveis.

Foram trabalhados principalmente:

- pH;
- oxigênio dissolvido;
- salinidade;
- turbidez;
- transparência.

### 7.5 Cálculo de médias anuais

Foi utilizada a ideia de agrupamento por ano para calcular médias anuais dos parâmetros.

Exemplo conceitual:

```python
df_med['ano'] = df_med['data'].dt.year

media_anual = df_med.groupby('ano')[
    ['ph', 'oxigenio_dissolvido', 'salinidade', 'turbidez', 'transparencia']
].mean()
