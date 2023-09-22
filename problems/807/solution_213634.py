def conta_frases(frases):
    frases = frases.replace('!','.'). replace('?','.').replace('...','.')
    frases=frases.split('.')
    return len(frases)