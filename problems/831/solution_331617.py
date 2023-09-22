def lingua_p(portuga):
    i= 0
    final= ''
    portuga= portuga.lower()
    for x in range(len(portuga)):
        if portuga[i] in 'aeiouáéíóúãõ':
            final += portuga[i] + 'p' + portuga[i]
        i += 1
        return final