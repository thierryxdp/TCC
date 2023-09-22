def inverte(texto):
    '''funcao que dada uma frase, retorna uma outra frase que contenha a mesma frase so que na ordem inversa, sem letras maiusculas e pontuacoes
    str->str'''
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,'.',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,'?',' ')
    texto= str.replace(texto,'!',' ')
    reverso= (list.reverse(str.split(str.lower(texto)))
    return (reverso)