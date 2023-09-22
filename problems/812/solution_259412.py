def subs(letras):
    pont = ['.',',',':',';''-','!','?']
    if letras in pontos:
        return ''
    
    else:
        return letras
    
    def retira_pontu(letras):
        
        frases = ''.join(map(subs,letras))
        
        return frases