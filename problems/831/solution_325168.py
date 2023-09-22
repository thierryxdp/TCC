def vogal_num(palavra):
    '''define o numero de vogais de uma palavra;srt->int'''
    y=0
    j=len(palavra)
    listavogal=[]
    for k in range(j):
        if palavra[k] in 'aeiouAEIOUÃãÕõáéíóúàÀÁÉÍÓÚ':
            listavogal.append(palavra[k])
    return len(listavogal)
def lingua_p(palavra):
    '''recebe uma palavra e retorna a mesma palavra traduzida para a íngua do P; str->str'''
    lista=list(palavra)
    i=len(lista)
    for n in range(i+listavogal(palavra)):
        if lista[n] in 'aeiouAEIOUáéíóúÁÉÍÓÚÃã':
            list.insert(lista,n+1,'p'+lista[n])
    return str.lower(str.join('',lista))