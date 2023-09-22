def freq_palavras(frase):
    'função que recebe uma string e retorna dicionário, contendo cada palavra '
    'string como chave e, como valor, a quantidade de ocorrências da palavra'
    'string, dict'
    frase=frase.replace("–", " ").replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ")
    novafrase=(str.split(frase))
    dict={}
    #dict={novafrase[1]:5}
    n=0
    while n<len(novafrase):
        if novafrase[n] in dict:
            n+=1
        else:
            dict[novafrase[n]]=list.count(novafrase,novafrase[n])
            n+=1
    return dict