def freq_palavras(frase):
    """ Recece uma frase e retorna um dicionário com as palavras dessa frase que tenham seus respectivos valores como o número de vezes que essa palavra aparece na frase;
    string->dict """
    frase=frase.split()
    dic={}
    for i in frase:
        dic[i]=frase.count(i)
    return dic