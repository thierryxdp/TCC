def retira_pontuacao(x:str):
    if '...' in x:
        return str.count(x,'.')+str.count(x,'?')+str.count(x,'!')+str.count(x,'...')-3*str.count(x,'...')
    else:
        return str.count(x,'.')+str.count(x,'?')+str.count(x,'!')