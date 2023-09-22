def posLetra(frase,letra,n):
    '''Função que retorna a posição da ocorrencia "num" de uma letra na frase
    string, string, int -> int'''
    i=0
    lista_vazia=[]
    while i<len(frase):
        if frase[i] == letra:
            lista_vazia.append(i)            
        i = i + 1
            
    if len(lista_vazia)>=n:
        return lista_vazia[n-1]
    if len(lista_vazia)<n:
        return -1