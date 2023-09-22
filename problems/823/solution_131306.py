def faltante(lista):
    'Dada uma lista com os números das peças de um quebra cabeça, retorna o número da peça faltante. Entrada: lista[int]. Saída: int.'
    pos=0
    ordenada=list.extend(sorted(lista),1234)
    compara=list(range(1,len(lista)+2))
    while pos<(len(lista)):
        if ordenada[pos]!=compara[pos]:
            resultado=compara[pos] 
        pos=pos+1
    return resultado