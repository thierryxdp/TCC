def colchao(medidas, H,L):
"""São fornecidas as medidias de um colchão e deve-se construir um código que verifique se é possível o colchão atravessar uma porta cujas dimensões são H e L, sendo H a altura e L a largura da porta."""
"""list, int, int -> booleano"""


    A = medidas[0]   
    B = medidas[1]
    C = medidas[2]

    if (H >= B and L >= A):    #verificação passagem longitudinal do colchão
        return True
    elif (L >= B and H >= A):  #verificação passagem transversal do colchão
        return True
    elif (H >= C and L >= A):  #verificação passagem com a maior dimensão paralela à altura da porta
        return True
    else:
        return False