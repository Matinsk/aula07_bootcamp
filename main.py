from etl import leitor__csv,filtrar_produtos_nao_entregues,somar_valores_dos_produtos

path_arquivo = "vendas.csv"

lista_de_produtos = leitor__csv(path_arquivo)
produtos_nao_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_total_produtos = somar_valores_dos_produtos(lista_de_produtos)
print(produtos_nao_entregues)
print(valor_total_produtos)