"""
Exemplo conceitual de etapas usadas no estudo de caso.

Este arquivo não reproduz integralmente o notebook original do estágio.
Ele resume algumas etapas técnicas documentadas:
- seleção de colunas;
- padronização;
- conversão de datas;
- remoção de registros incompletos;
- cálculo de médias anuais;
- matriz de correlação.

Para reprodução completa, seria necessário recuperar as bases e notebooks originais.
"""

import pandas as pd
import matplotlib.pyplot as plt


COLUNAS_INTERESSE = [
    "Data Coleta",
    "Latitude",
    "Longitude",
    "pH",
    "Oxigênio Dissolvido (mg/L)",
    "Salinidade (ppt)",
    "Turbidez (UNT)",
    "Transparência da Água (m)"
]


COLUNAS_PADRONIZADAS = [
    "data",
    "latitude",
    "longitude",
    "ph",
    "oxigenio_dissolvido",
    "salinidade",
    "turbidez",
    "transparencia"
]


def preparar_base(df):
    """
    Recebe um DataFrame bruto e retorna uma versão padronizada
    para análise exploratória.
    """

    df = df[COLUNAS_INTERESSE].copy()
    df.columns = COLUNAS_PADRONIZADAS

    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    df = df.dropna(subset=["data"])

    df = df.dropna(
        subset=[
            "ph",
            "oxigenio_dissolvido",
            "salinidade",
            "turbidez",
            "transparencia"
        ],
        how="all"
    )

    return df


def calcular_medias_anuais(df):
    """
    Calcula médias anuais dos parâmetros ambientais.
    """

    df = df.copy()
    df["ano"] = df["data"].dt.year

    media_anual = df.groupby("ano")[
        [
            "ph",
            "oxigenio_dissolvido",
            "salinidade",
            "turbidez",
            "transparencia"
        ]
    ].mean()

    return media_anual


def plotar_tendencias(media_anual):
    """
    Gera gráfico de tendência anual dos parâmetros.
    """

    plt.figure(figsize=(10, 6))

    for col in media_anual.columns:
        plt.plot(
            media_anual.index,
            media_anual[col],
            label=col,
            linewidth=2
        )

    plt.title("Tendência anual dos parâmetros de qualidade da água")
    plt.xlabel("Ano")
    plt.ylabel("Média anual")
    plt.legend(title="Parâmetros")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def calcular_correlacao(df):
    """
    Calcula matriz de correlação entre os principais parâmetros.
    """

    corr = df[
        [
            "ph",
            "oxigenio_dissolvido",
            "salinidade",
            "turbidez"
        ]
    ].corr()

    return corr
