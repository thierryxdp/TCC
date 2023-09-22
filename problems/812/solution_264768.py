def retira_pontuacao(frase):
    """Função que dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituidos"""
    pontuacao = str(' ')
    frase = str.replace(frase,'_',pontuacao)
    frase = str.replace(frase,'-',pontuacao)
    frase = str.replace(frase,'.',pontuacao)
    frase = str.replace(frase,',',pontuacao)
    frase = str.replace(frase,':',pontuacao)
    frase = str.replace(frase,';',pontuacao)
    return frase