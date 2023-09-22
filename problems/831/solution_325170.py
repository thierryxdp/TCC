def lingua_p(palavra):
    '''recebe uma palavra em português e retorna a palavra traduzida para
    a língua do P.
    str ->str'''
    i =0
    nova =''
    while i <len(palavra):
        if palavra[i] in 'AEIOUaeiouáÁóÓíÍãÃ':
            nova +=palavra[i] +'p'+str.lower(palavra[i])
        else:
            nova +=str.lower(palavra[i])
        i +=1
        
    return nova