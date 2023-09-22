# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista = frase.split(" ",)
    if lista [0] == "":
        return (len(lista)-1)
    elif lista [-1] == "":
        return (len(lista)-1)
    elif lista[-1]=="" and lista[0]=="":
        return (len(lista)-2)
    else:
        return len(lista)