def lingua_p(portuga):
    i= 0
    final= ''
    for x in range(len(portuga)):
        if portuga[i] in 'aeiouáéíóúãõ':
            final += portuga[i] + 'p' 
        else: 
            final += portuga[i]
        i += 1
        return final