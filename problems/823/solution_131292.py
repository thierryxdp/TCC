def falta_peca(lista):
    'Dada uma lista com os números das peças de um quebra cabeça, retorna o número da peça faltante. Entrada: lista[int]. Saída: int.'
    pos=0
    ordenada=sorted(lista)
    compara=list(range(1,len(lista)))
    while pos<(len(lista)-1):
        if compara[pos]!=ordenada[pos]:
            resultado=compara[pos]
        pos=pos+1
    return resultado