def retira_pontuacao(frases):
    '''comente'''
    funcao=str.split(frases)
    func=len(frases)
    return str.replace(frases,'.',' ') or str.replace(frases,'!',' ')