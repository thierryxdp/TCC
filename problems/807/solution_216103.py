def conta_frases(s):
    return len(s.replace('...','.').replace('?','.').replace('!','.').split('.'))