def posLetra(palavra,letra,num):
    '''
        Dada uma string retorna o index da ocorrencia (num) de um dado caracter.
        str,str,int -> int
    '''
    if num > str.count(palavra,letra):
        return -1
    i=0
    onde=[]
    while i<len(palavra):
        if palavra[i] == letra:
            onde=onde + [str.index(palavra,palavra[i],i)]
        if len(onde) == num:
            return onde[-1]
        i = i+1
    return onde[-1]