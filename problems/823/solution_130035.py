def faltante(lista):
    """ Retorna o número da peça sumida na lista; list -> int """
    lista.sort();
    i=0;
    l=[];
    while i<len(lista)-1:
        if lista[i+1]-lista[i]>1:
            return i+2;
        i+=1;
    if lista[0]==1:
        return lista[-1]+1;
    else:
        return lista[0]-1;