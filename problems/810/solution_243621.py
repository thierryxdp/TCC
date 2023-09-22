def retira_pontuacao(frase):
    """dada uma frase, a função retorna a mesma frase com todos os caractere de pontuação
    substituídos por espaço;
    str->str"""
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'-',' ')
    return frase

def inverte(frase):
    """dada uma frase, a função retorna uma outra frase que contenha as mesmas palavras da frase
    de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação;
    str->str"""
    A= retira_pontuacao(frase)
    A= list(str.lower(A))
    A= list.reverse(A)
    return A