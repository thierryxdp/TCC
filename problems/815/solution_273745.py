def inverte(frase):
    ''' funcao que recebe uma frase em string e retorna
        o inverso da frase, sem as pontuacoes e com letras 
        minusculas, utilizando as funcoes 'lower', 'replace',
        'split', 'reverse' e 'join'
        str -> str'''
    frase= frase.lower()
    x= frase.replace('.',' ')
    x= x.replace('?',' ')
    x= x.replace(',',' ') 
    x= x.replace('-',' ')
    x= x.replace('!',' ')
    x= x.split()
    x.reverse()
    return str.join(' ',x)