def colchao(medidas,H,L):
    ''' Recebe as medidas do colchão e da porta e retorna se é possivel passar com o colchão pela porta'''
    A,B = medidas[0],medidas[1] #Converte os dados em variavel
    if B <= H and A <= 100: #Compara se é possivel passar com o colchão pela porta
        return True #se passar retorna True
    else:
       return False #se não retorna False