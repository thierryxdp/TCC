def lingua_p(palavra):
    '''retorna a palavra traduzida para a lingua do P;
str->str'''

    i=0
    traducao=''

    for exemplos in palavra:
        if palavra[i] in 'AEIOUaeiou':
            traducao=traducao+(str.lower(palavra[i])+'p'+str.lower(palavra[i]))
            i=i+1
        else:
            traducao=traducao+str.lower(palavra[i])
            i=i+1
            
    return traducao