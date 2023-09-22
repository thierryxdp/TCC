def retira_pontuacao(frase):
    '''função que recebe uma frase(string) e retorna esta mesma frase porém com
todos os caracteres de pontuação substituídos por espaço (' '); string->string'''

    frase2=str.replace(frase,'...',' ')
    frase3=str.replace(frase2,'.', ' ')
    frase4=str.replace(frase3,'!',' ')
    frase5=str.replace(frase4,'?',' ')
    frase6=str.replace(frase5,',',' ')
    frase7=str.replace(frase6,';',' ')
    frase8=str.replace(frase7,':',' ')
    frase9=str.replace(frase8,'-',' ')
    frase10=str.replace(frase9,'–',' ')

    return frase10