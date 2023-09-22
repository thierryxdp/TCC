import string.upper
def uppCons(frase):
    '''retorna uma frase com todas as suas consoantes em maiúsculas
    entrada: str
    saída: str
    '''
    i=0
    upperfrase= ''
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU ;:,.!?""-ÃãÁáÀéÉêÊÍíôÔóÓúÚüÜº°':
            upperfrase= upperfrase + string.upper(frase[i])
        i=i+1
    return upperfrase