def retira_pontuação(frase):
    '''função que, dada uma frase, retorne a frase onde todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.
    entrada: string
    saída: string'''
    var1= str.join(' ',(str.slipt(frase,'-')))
    var2= str.join(' ',(str.split(var1,',')))
    var3= str.join(' ',(str.split(var2,':')))
    var4= str.join(' ',(str.split(var3,'.')))
    var5= str.join(' ',(str.split(var4,';')))
    return var5