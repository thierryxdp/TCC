def lingua_p(p):
    y=''
    for x in p:
        y=y+x
        if x in 'aeiouáé':
        	y=y+'p'+x
    return y