def inverte(frase):

	pto_final = frase.replace('.', ' ')
    interrogacao = pto_final.replace('?', ' ')
    exclamacao = interrogacao.replace('!', ' ')
    travessao = exclamacao.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_ptos = virgula.replace(':', ' ')
    pto_virgula = dois_ptos.replace(';', ' ')
    
    frase_minuscula = str.lower(pto_virgula)
    frase_separada = frase_minuscula.split()
    frase_invertida = frase_separada.reverse()
    
    return str.join(' ',frase_separada)