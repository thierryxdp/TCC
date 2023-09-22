def retira_pontuacao(frase):
    '''funcao que, dada uma frase, remove todos as pontuacoes, substituindo-as por espaco;
    str->str'''
    frase1=str.replace(frase,'!',' ')
    frase2=str.replace(frase1,'?',' ')
    frase3=str.replace(frase2,'...',' ')
    frase4=str.replace(frase3,'-',' ')
    frase5=str.replace(frase4,',',' ')
    frase6=str.replace(frase5,':',' ')
    frase7=str.replace(frase6,';',' ')
    frase8=str.replace(frase6,'.',' ')
    return frase8

def inverte(frase8):
    '''funcao que, dada uma frase sem os caracteres de pontuacao, retorna uma nova frase
    na ordem inversa e apenas com letras minusculas;
    str->str'''
    minusculo=str.lower(frase8)
    nova=(str.split(minusculo))[::-1]
    return str.join('',nova)