def retira_pontuacao(x=""):
    '''função que substitui pontuações na frase por espaços'''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return x

▪︎def insere(x,n):
    '''função que dada uma lista em ordem crescente de números inteiros e
    um número inteiro n, inclua n na posição certa'''
    list.append(x,n)
    list.sort(x)
    return x

▪︎def conta_frases(x):
    '''função que conta o número de frases que aparecem no texto, segundo as
    pontuações ali presentes'''
    a=str.count(x,'!')+str.count(x,'?')
    b=str.count(x,'...')
    c=str.count(x,'.')
    d=c-(3*b)
    return a+b+d