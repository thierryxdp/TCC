def faltante(lista):
    'Dada uma lista com os números das peças de um quebra cabeça, retorna o número da peça faltante. Entrada: lista[int]. Saída: int.'
    pos=0
    ordenada=sorted(lista)
    compara=list(range(1,len(lista)))
    while pos<(len(lista)):
        if ordenada[pos]!=compara[p]:
            resultado=compara[pos]
        pos=pos+1
    return resultado