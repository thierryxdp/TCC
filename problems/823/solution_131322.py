def faltante(lista):
    'Dada uma lista com os números das peças de um quebra cabeça, retorna o número da peça faltante. Entrada: lista[int]. Saída: int.'
    pos=0
    ordenada=sorted(lista)
    compara=list(range(1,len(lista)+2))
    resultado=0
    while pos<(len(lista)) and resultado!=1:
        if ordenada[pos]!=compara[pos]:
            resultado=resultado+int(compara[pos])
        pos=pos+1
   
    return resultado