def acima_da_media(notas):
    """Dada uma lista com as notas dos alunos, retorna uma lista mostrando
       todas as notas acima da média lista -> lista"""
    varredura = 0
    listaf = []
    while varredura <= len(notas):
        if lista[varredura] > sum(notas)/int(len(notas)):
            listaf = listaf + lista[varredura]
            varredura += 1 
            return listaf