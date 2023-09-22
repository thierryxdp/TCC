import string
def uppCons(frase):
    '''retorna uma frase com todas as suas consoantes em maiúsculas
    entrada: str
    saída: str
    '''
    i=0
    upperfrase= ''
    while i<len(frase):
        letraemquestao=frase[i]
        if frase[i] not in 'aeiouAEIOU ;:,.!?""-ÃãÁáÀéÉêÊÍíôÔóÓúÚüÜº°':
            upperfrase= upperfrase + letraemquestao.upper()
        else:
            upperfrase= upperfrase + letraemquestao
        i=i+1
    return upperfrase