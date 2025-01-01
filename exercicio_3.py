#Contar Valores Únicos em uma Lista

lista_valores = [20,30,40,50,60,70,80,80,90]

def contar_valores_unicos(lista : list[float]) -> list[float]:
    return print(len(set(lista_valores)))

contar_valores_unicos(lista_valores)