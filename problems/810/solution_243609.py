def inverte(texto):
    '''funcao que dada uma frase(texto), retorna uma outra frase que contenha a mesma frase so que na ordem inversa, sem letras maiusculas e pontuacoes
    str->str'''
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,'.',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,'?',' ')
    texto= str.replace(texto,'!',' ')
    texto2=(str.split(str.lower(texto))
    reverso = list.reverse(texto2)
    return reverso