def maiores (listaNum, n):
   '''Função que retorna nova lista com todos os numeros maiores que n,
    em ordme crescente
    list, int => list''''
    maiores=listaNum[0]
    n=listaNum[1]
    maiores.append(n)
    if max(maiores)==n:
        return []
    else:
        ordem_decrescente= ordem_decrescente.sort(listaNum)
        return ordem_decrescente