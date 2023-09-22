def lingua_p(palavra):
    """ Dada uma palavra retorna uma nova palavr traduzidda para ligua do p. EX: entao -> epentapaopo.
     	entrada string -> saida string"""
    
    traducao  = ""
    
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            traducao = traducao + letra + 'p' + letra
        else: 
            traducao = traducao + letra
    return traducao