def freq_palavras(frases):
    """Recebe uma string e retorna uma dicionário onde cada palavra da
string seja uma chave e também quantas vezes a palavra aparece"""

    dic={}
    tempdic={}
    
    palavra = frases.split(' ')
    for i in range(0,len(palavra)):
        if palavra[i] in dic:
            dic[palavra[i]]+=1
            i=i+1
        else:
            tempdic = {palavra[i]:1}
            dic.update(tempdic)
            i=i+1
    return dic