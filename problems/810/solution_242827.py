def retira_pontuacao(fraseint):
    '''
        recebe uma frase e retorna a mesma frase suprimindo todo caracter de
        pontuacao
        entrata: string
        saida: string
    '''
    fraseint=str.replace(fraseint,'_',' ')
    fraseint=str.replace(fraseint,'_',' ')
    fraseint=str.replace(fraseint,',',' ')
    fraseint=str.replace(fraseint,':',' ')
    fraseint=str.replace(fraseint,';',' ')
    fraseint=str.replace(fraseint,'.',' ')
    fraseint=str.replace(fraseint,'?',' ')
    fraseint=str.replace(fraseint,'!',' ')
    fraseint=str.replace(fraseint,'...',' ')
    return fraseint


def inverte(frase):
    '''
        recebe uma frase e retorna uma frase com as mesmas palavras na orde
        inversa e sem pontuacao e sem letras maiusculas
        entrada: string
        saida: string
    '''
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    frase=str.split(frase)
    frase=frase[::-1]
    frase=str.join(' ',frase)
    return frase