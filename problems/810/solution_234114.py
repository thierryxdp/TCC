def retira_pontuacao(frase):
    '''Função que, dada uma frase, retorne a frase onde todos os caracteres
    de pontuação tenham sido substituídos por espaço
    str -> str
    '''
    etapa1 = str.replace(frase,'-',' ')
    etapa2 = str.replace(etapa1,',',' ')
    etapa3 = str.replace(etapa2,':',' ')
    etapa4 = str.replace(etapa3,';',' ')
    etapa5 = str.replace(etapa4,'!',' ')
    etapa6 = str.replace(etapa5,'?',' ')
    etapa_final = str.replace(etapa6,'.',' ')

    return etapa_final

def inverte(texto):
    '''Função que, dada uma frase, retorne uma nova frase que contenha as
    mesmas palavras da frase de entrada na ordem inversa, sem letras 
    maiúsculas e sem pontuação
    str -> str
    '''
    fase1 = retira_pontuacao(texto)
    fase2 = str.join(' ',str.split(remove_pont(etapa1))[::-1])
    fase_final = str.lower(etapa2)

    return fase_final