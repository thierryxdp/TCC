import re 
def conta_frases(t):
    ''
    txt= t.replace('?','x')
    txt2= txt.replace('!','x')
    txt3= txt2.replace('.','x')
    txt4= txt3.replace('...','x')
    txt5= txt4.replace('xxx','x')
    return len((txt5.split('x ')))