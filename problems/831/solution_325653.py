def lingua_p(palavra):
    final = ''
    for i in len(palavra):
        if palavra[i] in 'aAàÀáÁãÃeEéÉêÊiIíÍoOóÓôÔõÕuUúÚ':
            x= palavra[i]+'p'+palavra[i]
            final = final + x
        else:
            final = final + palavra[i]
    return str.lower(final)