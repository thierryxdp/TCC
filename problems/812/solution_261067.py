def retira_pontuacao(fraseint):
    '''
        recebe uma frase e retorna a mesma frase suprimindo todo caracter de
        pontuacao
        entrata: string
        saida: string
    '''
    fraseint=str.replace(fraseint,'_',' ')
    fraseint=str.replace(fraseint,'-',' ')
    fraseint=str.replace(fraseint,',',' ')
    fraseint=str.replace(fraseint,':',' ')
    fraseint=str.replace(fraseint,';',' ')
    fraseint=str.replace(fraseint,'.',' ')
    fraseint=str.replace(fraseint,'?',' ')
    fraseint=str.replace(fraseint,'!',' ')
    fraseint=str.replace(fraseint,'...',' ')
    return fraseint