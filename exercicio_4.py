#Converter Celsius para Fahrenheit em uma Lista
#Formula = (0 °C × 9/5) + 32

lista_de_temperatura = [32,31,40,28,21,10,11,28]



def converter_celsius_para_fahrenheite(lista : list[float]) -> list[float]:
    return print([round(temperatura * (9/5) + 32,2) for temperatura in lista_de_temperatura])

converter_celsius_para_fahrenheite(lista_de_temperatura)