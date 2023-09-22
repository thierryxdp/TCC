def lingua_p(palavra):
    '''retorna a palavra traduzida para a lingua do P;
str->str'''

    traducao=''

    for i in palavra:
        if i in 'AEIOUaeiouáéíóúÁÉÍÓÚÃã':
            traducao=traducao+(str.lower(i)+'p'+str.lower(i))
        else:
            traducao=traducao+str.lower(i)
            
    return traducao