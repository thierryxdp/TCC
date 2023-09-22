def retira_pontuação(frase):
    """dada uma frase, a função retorna a mesma frase, porém sem pontuação.
    string-->string
    
    Parâmetros
    frase: frase de entrada da qual será retirada a pontuação"""
    return str.replace(frase,"!","?",".",",","-",":",";"," ")