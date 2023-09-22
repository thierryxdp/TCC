def filtraMultiplos(lista,n):
    """Retorna uma lista contrndo todos os elementos da lista original que sejam divisíveis por n;
    list,float->ist"""
    resposta=[]
    pisicao=0
    while posicao<len(lista):
        if lista[posicao]%n==0:
            resposta=resposta+lista[posicao]
        posicao=posicao+1
        return resposta