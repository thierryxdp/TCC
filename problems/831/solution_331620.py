def lingua_p(portuga):
    x= 0
    final= ''
    portuga= portuga.lower()
    for x in range(len(portuga)):
        if portuga[x] in 'aeiouáéíóúãõ':
            final += portuga[x] + 'p' 
        else: 
            final += portuga[x]
        x += 1
        return final