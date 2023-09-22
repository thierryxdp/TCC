def lingua_p(palavra):
    '''traduz uma palavra para a lingua do p  str->"p str"'''
    palavra_traduzida = ''
    for letra in palavra:
        
        if letra in 'aeiouáéúãõâêîôûAEIOUÁÉÚÃÕÂÊÎÔÛ':
            palavra_traduzida += letra + 'p' + letra
        
        else:
            palavra_traduzida += letra
    
    return palavra_traduzida