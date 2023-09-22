def retira_pontuaçao(frase):
    """Função que dada uma frase, retorna a frase onde os caracteres de 
    pontuação, incluindo travessão, dois pontos, ponto e vírgula e ponto
    final que são substituídos por espaço.
    str -> str
    """
    
    return str.replace(str.replace(str.replace(str.replace(frase.replace(',',' '),'.',' '),':',' '),';',' '),'-',' '))