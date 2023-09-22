def posLetra(string,letra,numero):
    "função que recebe uma strind,uma letra e um numero,e retorna a posição da string aquela ocorrencia da letra.  str,str,int->int."
    while numero <=str.count(string,letra):
        a=str.index(string,letra,numero)
        return a
    if numero > str.count(string,letra):
        return -1