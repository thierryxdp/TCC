#A função recebe uma frase
#1-necessário transformá-la em uma lista
#2-Inverter a ordem 
#3-voltar a uma string
#4-retonar a string
def inverte(frase: str)->str:
    ListaFrase=str.split(frase)
    list.reverse(ListaFrase)
    return str.join(" ", ListaFrase)