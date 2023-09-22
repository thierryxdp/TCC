def freq_palavras(frase):
    """ Recece uma frase e retorna um dicionário com as palavras dessa frase que tenham sesu respectios valores como o número de vezes que essa palavra aparece na frase;
    string->dict """
    frase=frase.split()
    i=0
    dic={}
    for i in range(len(frase)):
        dic[frase[i]]=frase.count(frase[i])
    return dic