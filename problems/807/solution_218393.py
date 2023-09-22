def conta_frases(frase):
    '''conta quantas frases a string tem.
    	str -> int'''
    qnt_palavras = 0
    numero_do_digito = 0
    for digito in frase:
        if (digito == '!' or digito == '?'):
            '''vendo quantas frases terminam com ! ou ?)'''
            qnt_palavras += 1
        if digito == '.':
          	'''se temos um ., temos que verificar se sao reticencias ou ponto final.'''
            if numero_do_digito + 1 < len(frase) and numero_do_digito - 1 >= 0:
               
                if frase[numero_do_digito + 1] != '.' and frase[numero_do_digito - 1] != '.':
                    '''é um ponto final'''
                    qnt_palavras += 1
                if frase[numero_do_digito - 1] == '.':
                    '''sao reticencias'''
                    qnt_palavras +=1
        numero_do_digito +=1
    return qnt_palavras