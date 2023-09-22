def inverte(frase):
    ''' Função que recebe uma frase e retorna a mesma ao contrário
        e sem as pontuações como: (,)(-)(:)(;)(?)(!)(.)
        : param frase: str
        : return: str
    '''
    frase=frase.replace(',',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    frase= frase.split()
    frase= frase[::-1]
    return ((((','.join(frase)).replace(',',' ')).lower())).strip()