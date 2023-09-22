def retira_pontuacao(texto):
    '''funcao que dado um texto retira e substitui as pontuacoes
por espacos; str -> str'''
    novo_texto = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'-',' '),':',' '),';',' '),'?',' '),'!',' '),'.',' '),',',' ')
    return novo_texto

def inverte(frase):
    '''funcao que recebe uma frase e converte as letras
maiusculas em minusculas alem de inverter a frase e tirar
a pontuacao; str -> str'''
    A = str.split(str.lower(retira_pontuacao(frase)))
    list.reverse(A)
    B = ','.join(A)
    C = str.replace(B,',',' ')
    return C