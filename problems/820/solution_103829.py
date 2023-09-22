def posLetra(s,l,n):
    'Função que recebe uma string, uma letra e um número de ocorrência dessa string, para retornar em que posição houve essa ocorrência. Caso existam menos ocorrências da letra, é retornado -1.'
    'str,str,int->int'
    
    c=0
    a=0
    b=len(s)
    lista=[]
    while a!=b:
        z=str.find(s,l,c,c+1)
        lista=lista+[z]
        a=a+1
        c=c+1
    list.sort(lista)
    while -1 in lista:
        list.remove(lista,-1)
    if n>len(lista):
        return -1
    else:
        return lista[n-1]