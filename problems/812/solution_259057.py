def retira_pontuacao(frase):
    """Função que dada uma frase retorna a mesma com
       a pontuação substituída por espaço."""
    frase1 = str.split(frase, '-')
    frase2 = frase1 + str.split(frase,':')
    frase3 = frase2 + str.split(frase,',')
    frase4 = frase3 + str.split(frase,';')
    frase5 = frase4 + str.split(frase,'.')
    frase6 = frase5 + str.split(frase,'?')
    frase7 = frase6 + str.split(frase,'!')
    frase = str.split(frase,'frase7')
    return frase