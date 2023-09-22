def lingua_p(palavra):
    '''traduz uma palavra para a lingua do p  str->"p str"'''
    for letra in palavra:
        
        if letra in 'aeiouáéúãõâêîôûAEIOUÁÉÚÃÕÂÊÎÔÛ':
            palavra_traduzida += p + letra
        
        else:
            palavra_traduzida += letra
    
    return palavra_traduzida