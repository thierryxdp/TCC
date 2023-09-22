def conta_frases(x):
    if '!' in x:
        exclatro=str.replace(x,'!','*')
        exclafra=str.count(exclatro,'*')
        pontfra=str.count(exclatro,'.')
        retfra=str.count(x,'...')
        pergfra=str.count(x,'?')
        return pergfra+exclafra+pontfra+retfra
    else:
        return pontfra+retfra+pergfra