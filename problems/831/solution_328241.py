def lingua_p(palavra):
    '''Função que retorna uma mesma palavra traduzida
    para a língua do P.
    pala=str->str'''
    resultado=[]
    for letra in palavra:
        letra=str.lower(letra)
        if letra in 'aeiouãâáàéêôõóúûíî':
            x=letra+'p'+letra
            list.append(resultado,x)
        else:
            list.append(resultado,letra)
    return str.join('',resultado)