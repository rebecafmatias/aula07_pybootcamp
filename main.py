"""Desafio: Análise de Vendas de Produtos Objetivo:
Dado um arquivo CSV contendo dados de vendas de produtos, 
o desafio consiste em ler os dados, processá-los em um dicionário para análise e,
por fim, calcular e reportar as vendas totais por categoria de produto.
"""

# 1. Ler CSV e processar dados

def ler_e_processar_dados_csv(path_csv):

    import csv

    file_path: str = path_csv
    dados_lista: list = []
 

    with open(file = file_path, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)

        for i in leitor_csv:
            dados_lista.append(i)

    return dados_lista


# 2. Calcular vendas

def calcular_vendas_total (dados_venda: list) -> dict:

    total_vendido_por_categoria: dict = {}

    for venda in dados_venda:
        if venda['categoria'] not in total_vendido_por_categoria:
            total_vendido_por_categoria.update({venda['categoria']: float(venda['valor'])})
        else:
            total_vendido_por_categoria[venda['categoria']] += float(venda['valor'])
    
    return total_vendido_por_categoria

path: str = 'vendas.csv'
dados_de_vendas: list = ler_e_processar_dados_csv(path)
total_vendido: dict = calcular_vendas_total(dados_de_vendas)
