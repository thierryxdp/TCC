def conta_frases(frase):
    return str.count(str.replace(frase,'...','@'),'.')str.count(frase,'?')+str.count(frase,'!')+str.count(str.replace(frase,'...','@'),'@')