def retira_pontuacao(frase):
    """Dado uma frase, a função retorna todos os caracteres de pontuação
    da mesma subsituídos por espaços.
    Parametros de entrada: str
    Retorna: Str"""


    auxiliar= frase.replace('.',' ')
    auxiliar= auxiliar.replace('...',' ')
    auxiliar= auxiliar.replace('?',' ')
    auxiliar= auxiliar.replace('!',' ')
    auxiliar= auxiliar.replace(':',' ')
    auxiliar= auxiliar.replace(',',' ')
    auxiliar= auxiliar.replace(';',' ')
    auxiliar= auxiliar.replace('-',' ')

    return auxiliar