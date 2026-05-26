# Análise de Dados Ambientais da Lagoa dos Patos

Estudo de caso técnico baseado em estágio obrigatório realizado com foco em tratamento, organização e visualização de dados ambientais da Lagoa dos Patos utilizando Python, Jupyter Notebook, pandas e Matplotlib.

> **Status:** documentação técnica reconstruída a partir de registros do estágio, relatório e material de apresentação científica.  
> Os notebooks, bases tratadas e gráficos originais não estão integralmente disponíveis nesta versão pública.

---

## 1. Visão geral

Este repositório documenta um projeto de análise de dados ambientais desenvolvido durante estágio obrigatório, com foco na qualidade da água da Lagoa dos Patos, no Rio Grande do Sul.

O trabalho utilizou dados públicos da FEPAM e da ANA/RNQA para investigar parâmetros físico-químicos da água, como pH, oxigênio dissolvido, salinidade, turbidez e transparência.

A análise foi realizada em ambiente Jupyter Notebook, utilizando Python e bibliotecas voltadas para manipulação e visualização de dados.

---

## 2. Objetivo do projeto

O objetivo principal foi aplicar técnicas de programação e análise de dados para:

- coletar e organizar dados públicos ambientais;
- ler arquivos em formatos CSV e XLS;
- tratar problemas de encoding e padronização;
- filtrar estações associadas à Lagoa dos Patos;
- limpar e estruturar dados de qualidade da água;
- calcular médias anuais de parâmetros ambientais;
- criar gráficos de tendência;
- construir matrizes de correlação;
- apoiar a elaboração de relatório técnico e banner científico.

---

## 3. Contexto

A Lagoa dos Patos é um sistema lagunar de grande importância ambiental, social e econômica para o Rio Grande do Sul.

Por receber influência de rios, do Lago Guaíba e do Oceano Atlântico, seus parâmetros de qualidade da água podem variar ao longo do tempo devido a fatores como:

- regime de chuvas;
- entrada de água doce;
- influência marinha;
- enchentes;
- ressuspensão de sedimentos;
- atividades humanas;
- sazonalidade.

O projeto teve caráter exploratório, buscando organizar dados públicos e gerar visualizações iniciais que ajudassem a compreender variações nos parâmetros analisados.

---

## 4. Fontes de dados

Durante o estágio foram utilizadas ou investigadas bases públicas relacionadas ao monitoramento da qualidade da água.

As principais fontes foram:

- **FEPAM** — Fundação Estadual de Proteção Ambiental do Rio Grande do Sul;
- **ANA/RNQA** — Agência Nacional de Águas e Saneamento Básico / Rede Nacional de Monitoramento da Qualidade da Água;
- bases de estações de monitoramento;
- bases de medições físico-químicas;
- arquivos CSV e XLS.

Entre os arquivos trabalhados ou mencionados no fluxo do projeto estavam:

- `IQ_OD_2021.csv`;
- `Rede_Nacional_de_Monitoramento_da_Qualidade_da_Água_(RNQA)_-_Estações_implantadas_por_ano.csv`;
- `FEPAM_estacoes.csv`;
- `filtradas_fepam_LP.xls`;
- `FEPAM_estacoes_Lagoa.csv`;
- `fepam_lagoa_dos_patos_limpo.csv`.

---

## 5. Ferramentas e tecnologias

As principais ferramentas e bibliotecas utilizadas foram:

- Python;
- Jupyter Notebook;
- Anaconda;
- pandas;
- NumPy;
- Matplotlib;
- Seaborn;
- leitura de arquivos CSV/XLS;
- GitHub para documentação do projeto.

---

## 6. Estrutura planejada do projeto

A estrutura original do projeto foi organizada em pastas para separar dados brutos, dados tratados, notebooks e arquivos de relatório.

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
