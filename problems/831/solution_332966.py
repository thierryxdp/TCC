def lingua_p(palavra):
    '''retorna a palavra traduzida para a lingua do P;
str->str'''

    traducao=''

    for i in palavra:
        if i in 'AEIOUaeiouáéíóúÁÉÍÓÚÃã':
            traducao=traducao+(str.lower(palavra[i])+'p'+str.lower(palavra[i]))
        else:
            traducao=traducao+str.lower(palavra[i])
            
    return traducao