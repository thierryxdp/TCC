def conta_frases (frase):
    '''Função que retira a pontuação de uma frase e substiti por espaço
    string -> string'''
    
    frases = frase.split('...')
    terminadores = ['!', '.', '?']
    
    while '' in frases:
        frases.remove('')
        
    quantidade = len(frases)
    
    for frase in frases:
        for terminador in terminadores:
            for pos,char in enumerate(frase):
                if(char==terminador):
                    quantidade - 1    
    return quantidade