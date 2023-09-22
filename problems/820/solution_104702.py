def posLetra(texto,letra,n):
    '''recebe uma string,uma letra e um numero q indica a ocorrencia desejada da letra.
    Deve retornar em que posição esta ocorrendo a letra,
    caso exista menos ocorrencias do que foi pedido retorna -1.str,str,int->int'''
    i=0
    lista=[]
    while i<len(texto):
        if letra==texto[i]:
            lista=lista+[i,]
        i=i+1
    if n>len(lista):
        return -1
    else:
        return lista[n-1]