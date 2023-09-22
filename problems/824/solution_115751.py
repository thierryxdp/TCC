def uppCons (frase):
    '''Dada uma frase, retorne todas as consoantes
    em maiúsculas;
    string -> string'''
    i = 0
    f = ''
    while i < len(frase):
   		 if frase [i] in 'qwrtypsdfghjklçzxcvbnm':
        	    f = f + frase[i].upper()
                i = i + 1
            else:
                f = f + frase[i]
                i = i + 1
    return f