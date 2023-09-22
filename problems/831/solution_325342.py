def lingua_p(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    palavra1 = []
    for i in palavra:
        if list.count(palavra1,i)==0:
            list.append(palavra1,i)
    for letra in palavra1:
        if letra in vogais:
            elemento = letra + 'p' + letra
            palavra = str.replace(palavra, letra, elemento)
    return palavra