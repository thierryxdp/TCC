def retira_pontuacao(n):
    n = n.replace('...',' ')
    n = n.replace('!',' ')
    n = n.replace('?',' ')
    n = n.replace('.',' ')
    n = n.replace('-',' ')
    n = n.replace(',',' ')
    n = n.replace(':',' ')
    n = n.replace(';',' ')
    return n
def inverte(m):
    M = retira_pontuacao(m)
    M = M.split()
    M = M[::-1]
    M = ' '.join(M)
    return M