def retira_pontuacao(frase):
    '''retira a pontuacao de uma frase e coloca espaços no lugar dos 
    antigos caracteres de pontuaçao;
    str->str'''
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    return frase

def de_tras_pra_frente(frase):
    '''retorna a frase mas com as palavras em ordem inversa;
    str->str'''
    frase=str.split(frase,' ')
    frase=frase[::-1]
    frase=str.join(' ',frase)

def inverte(frase):
    '''retorna uma frase com a ordem das palavras invertida(de trás pra frente)
    e substitui as letras maiusculas em minusculas , alem disso retira-se a pontuaçao;
    str->str'''
    return str.(de_tras_pra_frente(retira_pontuacao(frase))).lower