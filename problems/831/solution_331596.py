def lingua_p(palavra):
    '''função que retorna uma palavra traduzida para a lingua do p.
    palavra -> str
    return -> str'''
    traducao = ''
    vogais = 'aeiou'
    
    for letra in range(len(palavra)):
        
        if palavra[letra] in alfabeto:
            traducao += palavra[letra] + 'p' + palavra[letra]
            
        else:
            traducao += palavra[letra]