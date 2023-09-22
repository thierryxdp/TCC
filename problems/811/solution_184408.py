def colchao(lista, H,L):
"""São fornecidas as medidias de um colchão e deve-se construir um código que verifique 
se é possível o colchão atravessar uma porta cujas dimensões são H e L, sendo H a altura
e L a largura da porta."""

"""list, int, int -> booleano"""


    A = lista[0]
    B = lista[1]
    C = lista[2]

    if (H >= B and L >= A):
        return True
    elif (L >= B and H >= A):
        return True
    elif (H >= C and L >= A):
        return True
    else:
        return False