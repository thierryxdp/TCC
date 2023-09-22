def lingua_p(portuga):
    i= 0
    final= ''
    portuga= portuga.lower()
    for x in range(len(portuga)):
        if portuga[i] == 'aeiou':
            final += portuga[i] + 'p' + palavra[i]
        i += 1
        return final