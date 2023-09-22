def uppCons(frase):
    '''funcao que retorna a frase de entrada com todas as suas consoantes em maiusculo,
    enquanto os demais caracteres retornam iguais a como estavam originalmente.
    string -> string'''
    cons_maiuscula = ''
    caractere = 0
    vogais = 'AEIOUaeiou'
    while caractere < len(frase):
        if frase[caractere] not in vogais:
            cons_maiuscula = cons_maiuscula + str.upper(frase[caractere])
    	else:
            cons_maiuscula = cons_maiuscula + frase[caractere]
            
   		caractere = caractere + 1
    return cons_maiuscula