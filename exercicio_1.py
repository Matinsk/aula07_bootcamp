#Calcular Média de Valores em uma Lista

lista_de_numeros = [3,4,5,6,10,20]



def media(lista_de_valores : list) -> float:
    quantidade_itens = len(lista_de_valores)
    soma_dos_valores = sum(lista_de_valores)

    return soma_dos_valores / quantidade_itens

media_lista = media(lista_de_numeros)

print(media_lista)