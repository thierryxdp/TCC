def conta_frases(x):
    if '...' in x:
        rettro=str.replace(x,'...','*')
        retfra=str.count(rettro,'*')
        pontfra=str.count(rettro,'.')
        exclafra=str.count(x,'!')
        pergfra=str.count(x,'?')
        return pergfra+exclafra+pontfra+retfra
    else:
        pontfra=str.count(x,'.')
        exclafra=str.count(x,'!')
        pergfra=str.count(x,'?')
        return pontfra+exclafra+pergfra