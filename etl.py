
import csv

path_arquivo = "vendas.csv"

def leitor__csv(nome_do_arquivo : str) -> list[dict]:

    

    with open(nome_do_arquivo, mode = "r", encoding = "utf-8") as arquivo: 
        lista_de_itens = []
        leitor = csv.DictReader(arquivo)
        for item in leitor:
            lista_de_itens.append(item)
        return lista_de_itens

lista_de_itens_vendas = leitor__csv(path_arquivo)

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    lista_com_produtos_filtros = []
    for produto in lista:
        if produto.get("entregue") == "False":
            lista_com_produtos_filtros.append(produto)
        else:
            ...
    return lista_com_produtos_filtros


def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))
    
    return valor_total


lista_de_produtos = leitor__csv(path_arquivo)
produtos_nao_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_total_produtos = somar_valores_dos_produtos(lista_de_produtos)
print(produtos_nao_entregues)
print(valor_total_produtos)

