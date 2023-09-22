def conta_frases(x):
    x=x.replace('  ',' ')
    x=x.replace('   ',' ')
    x=x.replace(',  ',' ')
    x=x.replace('; ',' ')
    x=x.replace(': ',' ')
    x=x.replace('!  ',' ! ')
    x=x.replace(' !',' ! ')
    x=x.replace('!',' ! ')
    x=x.replace('? ',' ! ')
    x=x.replace('. ',' ! ')
    x=x.replace('... ',' ! ')
    x=x.split(' ! ')
    if x.count('!')>3:
        return len(x)
    else:
        return len(x)-1