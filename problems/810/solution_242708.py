def retira_pontuacao(frase):
    """funcao que retorna a frase de entrada onde todos os caracteres de pontuacao tenham sido substituidos por espaco
    str -> str"""
    a=frase
    a=str.replace(a,'-',' ')
    a=str.replace(a,',',' ')
    a=str.replace(a,';',' ')
    a=str.replace(a,'?',' ')
    a=str.replace(a,'!',' ')
    a=str.replace(a,':',' ')
    a=str.replace(a,'.',' ')
    a=str.replace(a,'...',' ')
    return a

def inverte(frase):
    """funcao que dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,
    sem letras maiusculas e sem pontuacao;
    str -> str"""
    string_sem_pontos=retira_pontuacao(frase)
    lista_manipulacao=str.split(string_sem_pontos)
    list.reverse(lista_manipulacao)
    string_nova=' '.join(lista_manipulacao)
    return str.lower(string_nova)