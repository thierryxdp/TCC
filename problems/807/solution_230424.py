def conta_frases(s):
    ls=str.count(s,'...')+str.count(s,'!')+str.count(s,'?')
    if('.' in s):
      	str.replace(s,'...','-')
    return str.count(s,'.')
    return 0