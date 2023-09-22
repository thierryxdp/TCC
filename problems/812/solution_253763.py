def retira_pontuacao(frase):
    '''retira pontuação recebe uma frase e devolve a mesma frase, porém no lugar das pontuações vem um espaço em branco.
    str-->str'''
    texto=str.replace(frase,'!',' ')
    texto=str.replace(texto,',',' ')
    texto=str.replace(texto,':',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,'...',' ')
    texto=str.replace(texto,'.',' ')
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,';',' ')
    return texto