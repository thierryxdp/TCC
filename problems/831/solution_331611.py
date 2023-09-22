def lingua_p(portuga):
    i= 0
    portuga= portuga.lower()
    for x in range(len(portuga)):
        if portuga[i] == 'aeiou':
            final= portuga[i] + portuga
        return final