valor_1 = 10
valor_2 = 45

def soma_valor(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    Uma função simples de soma de valores float que retorna um valor float
    """

    resultado_soma = valor_1_para_somar+valor_2_para_somar
    return resultado_soma

valor_3 = soma_valor(valor_1,valor_2)
print(valor_3)