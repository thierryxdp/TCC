def eh_quadrada(m):
    """considerando uma função dada retornaum valor boleano
    identificando se essa é quadrada"""
    quantidade=len(m)
    funcao=[]
    if m==[]:
        return True
    for numero in range(quantidade):
        quantidade1=len(m[numero])
        list.append(funcao,quantidade1)
    if sum(funcao)==(len(m[0])**2):
        return True
    else:
        return False