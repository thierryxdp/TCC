def lingua_p(palavra):
    '''recebe como parâmetro uma palavra 
e retorna esta mesma palavra traduzida 
para a língua do P.'''
    palavrap=''
    for letra in range(len(palavra)):
        if palavra[letra] in 'AEIOUaeiouÁÉÍÓÚáéíóúÂÊÎÔÛâêîôû':
            palavrap = palavrap + palavra[letra] + 'p' + palavra[letra]
        if palavra[letra] not in 'AEIOUaeiouÁÉÍÓÚáéíóúÂÊÎÔÛâêîôû':
            palavrap = palavrap + palavra[letra]
    return palavrap