def conta_frase(frase):
    f1=frase.replace('.','x')
    f2=f1.replace('!','x')
    f3=f2.replace('?','x')
    f4=f3.replace('...','x')
    f5=f4.replace('xxx','x')
    
    return (len((str.split(f5,'x ')))