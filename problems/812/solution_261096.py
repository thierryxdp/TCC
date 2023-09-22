def retira_pontuacao(frase):
    '''Funcao que, dada uma frase, substitui todos os caracteres de pontuacao por espaco; str -> str'''
    if ',' in frase:
        return str.replace(frase,',','')
    if '.' in frase:
        return str.replace(frase,'.','')
    if '—' in frase:
        return str.replace(frase,'—','')
    if ':' in frase:
        return str.replace(frase,':','')
    if ';' in frase:
        return str.replace(frase,';','')