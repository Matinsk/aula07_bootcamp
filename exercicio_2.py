#Filtrar Dados Acima de um Limite

def filtrar_acima_limite(lista : list[float], limit : float) -> list[float]:
    lista_de_valores_acima = []
    for valor in lista:
        if valor > limit:
            lista_de_valores_acima.append(valor)
    
    return lista_de_valores_acima

lista_de_valores = [10,20,30,40,50,60,70,80,90,100]

lista_de_valores_acima = filtrar_acima_limite(lista_de_valores,40)

print(lista_de_valores_acima)