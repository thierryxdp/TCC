def filtra_pares(g):
    """Função que recebe uma tupla com quatro elementos inteiros como parâmetro, e retorna uma nova tupla contendo apenas os elementos pares da tupla original"""
    """tuple--->tuple"""
    # tvazia quer dizer tupla vazia
    tvazia=()
    if(g[0]%2)==0:
        tvazia=tvazia+(g[0],)
    if(g[1]%2)==0:
        tvazia=tvazia+(g[1],)
    if(g[2]%2)==0:
        tvazia=tvazia+(g[2],)
    if(g[3]%2)==0:
        tvazia=tvazia+(g[3],)
    return tvazia