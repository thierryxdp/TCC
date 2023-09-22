def lingua_p(palavra):
    '''funcao que recebe uma palavra e a traduz para a lingua do p;str->str'''
    traducao=''
    for i in palavra:
        if i in 'AEIOUaeiouáéíóúÁÉÍÓÚ':
            traducao=traducao+i+'p'+i
        else:
            traducao=traducao+i
    return traducao