def retira_pontuacao(frase0):

    '''função que dada uma frase retira toda a sua pontuação;

    str->str'''

    if ',' in frase0:

        frase0 = str.replace(frase0,',',' ')

    if '.' in frase0:

        frase0 = str.replace(frase0,'.',' ')

    if ';' in frase0:

        frase0 = str.replace(frase0,';',' ')

    if ':' in frase0:

        frase0 = str.replace(frase0,':',' ')

    if '!' in frase0:

        frase0 = str.replace(frase0,'!',' ')

    if '?' in frase0:

        frase0 = str.replace(frase0,'?',' ')

    if '-' in frase0:

        frase0 = str.replace(frase0,'-',' ')

    if '...' in frase0:

        frase0 = str.replace(frase0,'...',' ')

    return frase0