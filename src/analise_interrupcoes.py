import pandas as pd
from pathlib import Path


def carregar_dados(caminho_arquivo: Path) -> pd.DataFrame:
    """
    Lê o arquivo CSV de interrupções de energia e devolve um DataFrame.
    """
    df = pd.read_csv(caminho_arquivo)
    return df


def tratar_datas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte colunas de datas para o tipo datetime.
    """
    df["data_abertura"] = pd.to_datetime(df["data_abertura"])
    df["data_fechamento"] = pd.to_datetime(df["data_fechamento"])
    return df


def calcular_duracao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria coluna com a duração da ocorrência em minutos.
    Se a ocorrência ainda estiver em atendimento, deixa 0.
    """
    df["duracao_min"] = (
        df["data_fechamento"] - df["data_abertura"]
    ).dt.total_seconds() / 60

    # Ocorrências em atendimento ficam com NaN -> substitui por 0
    df["duracao_min"] = df["duracao_min"].fillna(0)
    return df


def salvar_dados_tratados(df: pd.DataFrame, caminho_saida: Path) -> None:
    """
    Salva o DataFrame tratado em um novo CSV.
    """
    df.to_csv(caminho_saida, index=False)


def gerar_resumos(df: pd.DataFrame) -> None:
    """
    Imprime alguns indicadores básicos no terminal.
    """
    print("\n==== Visão geral do dataset ====")
    print(df.head())

    print("\n==== Ocorrências por região ====")
    print(df.groupby("regiao")["id_ocorrencia"].count())

    print("\n==== Duração média (min) por causa (apenas concluídas) ====")
    concluidas = df[df["duracao_min"] > 0]
    print(concluidas.groupby("causa")["duracao_min"].mean().round(1))


def main():
    base_dir = Path(__file__).resolve().parent.parent  # pasta raiz do projeto

    caminho_raw = base_dir / "data" / "raw" / "interrupcoes_raw.csv"
    caminho_processado = base_dir / "data" / "processed" / "interrupcoes_clean.csv"

    print(f"Lendo dados de: {caminho_raw}")

    df = carregar_dados(caminho_raw)
    df = tratar_datas(df)
    df = calcular_duracao(df)

    gerar_resumos(df)
    salvar_dados_tratados(df, caminho_processado)

    print(f"\nArquivo tratado salvo em: {caminho_processado}")


if __name__ == "__main__":
    main()
