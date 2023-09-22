# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    a= str.split(frase," ")
    b= len(a)
    if frase[0]==" " and frase[-1]==" ":
        a= frase[1:-1]
        b= str.split(a," ")
        c= len(b)
        return c
    elif frase[0]==" ":
        a= frase[1:]
        b= str.split(a," ")
        c= len(b)
        return c
    elif frase[-1]==" ":
        a= frase[:-1]
        b= str.split(a," ")
        c= len(b)
        return c
    else:
        a= str.split(frase," ")
        b= len(a)
        return b