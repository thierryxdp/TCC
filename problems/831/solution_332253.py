def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    
    for letra in palavra:
       
        if letra == 'aeiou':
            palavra = palavra.join('p')
            
        return palavra