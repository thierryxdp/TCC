def posLetra (frase,letra,n):
    '''dada uma frase em sting, uma letra em string e um
    numero inteiro; é retornado pela funçao a posiçao
    da n ezima ocorrencia da letra na frase,
    porem se n for maior que o numero de vezes que a letra
    aparece na frase o valor retornado é -1
    str,str,int-->int'''
    i=0
    lista=[]
    if str.count(frase,letra)<n:
        return -1
    else:
        while i<len(frase):
        	if frase[i]==letra:
            	lista=lista+[str.index(frase,letra,i)]
            i=i+1
        return list.pop(lista,n-1)