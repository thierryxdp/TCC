def lingua_p(palavra):
    palavraComPe=''
    vogais ='aeiou'
    for letra in palavra.lower():
        palavraComPe+=letra
        if letra in vogais:
            palavraComPe+='p'+letra
    return palavraComPe