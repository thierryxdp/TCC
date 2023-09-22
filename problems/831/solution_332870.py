# Questão 3
def lingua_p (palavra_ptbr):
    '''Função que receberá uma palavra em portugues e nos retornará uma palavra na lingua do P'''

    palavra_ptbr = palavra_ptbr.lower()
    lingua_do_p = ''
    
    for letra in palavra_ptbr:
        
        if letra in 'aeiou':
           lingua_do_p += letra + 'p'+ letra
           
        else:
           lingua_do_p += letra
           
    return lingua_do_p