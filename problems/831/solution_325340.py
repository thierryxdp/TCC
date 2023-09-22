def lingua_p(palavra):
    vogais=['a','e','i','o','u','A','E','I','O','U']
    palavraP=[]
    for c in palavra:
        if list.count(palavraP,c)==0:
            list.append(palavraP,c)
    for letra in palavraP:
        if letra in vogais:
            elemento=letra+'p'+letra
            palavra=str.replace(palavra,letra,elemento)
        return palavra