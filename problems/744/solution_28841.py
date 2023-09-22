def hashtag(s):
    '''dada uma string s, retorna a mesma string com um '#' no início, no meio e no fim
    str-->str'''
    x=len(str(s))//2
    return "#"+str(s)[0:x]+"#"+str(s)[x+1:]+"#"