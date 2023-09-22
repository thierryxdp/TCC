def remove_pontuacao(frase):
    """essa função , dada uma frase(igual ao parâmetro de entrada frase), retorna a
frase onde todos os caracteres de pontuação foram substituídos por espaço.
string->string"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '), '?',' '),'!',' '),'-',' '),',',' '),';',' '),':',' ')

def inverte(frase):
    """essa função dada uma frase(igual ao parâmetro de entrada frase) retorna uma
outra frase que contém as mesmas palavras da frase de entrada na ordem inversa,
sem letras maiúsculas, e sem a pontuação.
string -> string"""
    lista=remove_pontuacao(frase)
    lista=str.lower(lista)
    lista=str.split(lista)
    list.reverse(lista)
    lista= str.join(' ', lista)
    return lista