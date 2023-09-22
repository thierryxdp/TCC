def lingua_p(palavra):
    
    '''Função que recebe uma palavra e traduz a mesma para a lingua do p. str -> str'''
    
    traducao = ''
    
    for i in palavra:
        if i in 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕãõÂÊÎÔÛâêîôû':
            traducao = traducao + i + 'p' + i
        else:
            traducao = traducao + i
            
    return traducao