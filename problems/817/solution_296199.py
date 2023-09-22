def maiores(l,n):
    '''
    Recebe uma lista (l) e um número (n). Insere n em l, ordena,
    recebe a posição inicial (k) e quantos tem (c). Exclui todos os 
    itens da lista até o k'ésimo elemento e seus posteriores. list, int -> list
    '''
    l.append(n); l.sort()
    k = l.index(n); c = l.count(n)
    del l[0:k+c]	
    return l

def acima_da_media(l):
    '''
    Efetua a soma (s) dos argumentos da lista. Mede o tamanho (t)
    da lista. Efetua a média (m). Chama a função maiores e recebe
    o resultado (r). Posteriormente retorna o resultado r.
    list -> list
    '''
    s = sum(l); t = len(l); m = s/t
    r = maiores(l,m)
    return r