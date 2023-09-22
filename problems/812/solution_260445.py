def retira_pontuacao(frase): 
    """funcao retorna a frase dada modificada com espaços nos lugares dos cracateres de pontuacao;
       str->str"""
    frase.replace ('-','')
    frase=frase.replace ('-','')
    frase.replace(',','')
    frase=frase.replace(',','')
    frase.replace(';','')
    frase=frase.replace(';','')
    frase.replace(':','')
    frase=frase.replace(':','')
    frase.replace(frase[-1],'')
    frase=frase.replace(frase[-1],'')
    return frase