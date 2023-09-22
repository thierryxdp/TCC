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
    y=x.split(' ! ')
    if x.count('!')>3:
        return len(y)
    else:
        return len(y)-1