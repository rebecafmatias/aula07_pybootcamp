"""1. Calcular Média de Valores em uma Lista"""

def calcular_media_lista_de_numeros(lista_de_valores: list) -> float:
    media_valores: float = sum(lista_de_valores)/len(lista_de_valores)

    return media_valores

lista_meus_numeros: list = [10,15,17,24,52,17]

media_meus_numeros: float = calcular_media_lista_de_numeros(lista_meus_numeros)

"""2. Filtrar Dados Acima de um Limite"""

def filtrar_valores_acima_do_limite(lista_de_valores: list, limite: float) -> list:
    valores_acima_do_limite = []
    for valor in lista_de_valores:
        if valor > limite:
            valores_acima_do_limite.append(valor)
    return valores_acima_do_limite

lista_meus_numeros: list = [10,15,17,24,52,17]
limite = 18
valores_acima_do_limite = filtrar_valores_acima_do_limite(lista_meus_numeros,limite)

"""3. Contar Valores Únicos em uma Lista"""

def contar_valores_unicos(lista_de_valores: list) -> int:
    return len(set(lista_de_valores))

lista_meus_numeros: list = [10,15,17,24,52,17]
qtd_valores_unicos = contar_valores_unicos(lista_meus_numeros)

"""4. Converter Celsius para Fahrenheit em uma Lista"""

def converter_celsius_para_fahrenheit(lista_de_valores: list) -> list:
    lista_temperatura_fahrenheit = []
    for i in lista_de_valores:
        temp_fahrenheit = (i*9/5)+32
        lista_temperatura_fahrenheit.append(temp_fahrenheit)

    return lista_temperatura_fahrenheit

lista_meus_numeros: list = [10,15,17,24,52,17]
lista_temperatura_f = converter_celsius_para_fahrenheit(lista_meus_numeros)



