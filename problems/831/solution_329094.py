def lingua_p(palavra):
    '''Fazer uma funcao que receba uma palavra(em portugues) e retorne a palavra substituindo a vogal por p mais a vogal original, tudo em minusculo;
    string -> string'''
    
    minusculo = str.lower(palavra)
    vogal = 'aeiouáéíóú'
    final = ''
    
    for letra in minusculo:
        if letra in vogal:
            final += letra + 'p' + letra
        
        else:
            final += letra
            
    return final