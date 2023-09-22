def conta_frases(x):
    y=x.replace('  ',' ')
    y=x.replace('   ',' ')
    y=x.replace(',  ',' ')
    y=x.replace('; ',' ')
    y=x.replace(': ',' ')
    y=x.replace('!  ',' ! ')
    y=x.replace(' !',' ! ')
    y=x.replace('!',' ! ')
    y=x.replace('? ',' ! ')
    y=x.replace('. ',' ! ')
    y=x.replace('... ',' ! ')
    y=x.split(' ! ')
    if x.count('!')>3:
        return len(y)
    else:
        return len(y)-1