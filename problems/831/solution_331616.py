def lingua_p(portuga):
    i= 0
    final= ''
    portuga= portuga.lower()
    for x in range(len(portuga)):
        if portuga[i] in 'aeiou':
            final += portuga[i] + 'p' + portuga[i]
        i += 1
        return final