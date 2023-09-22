def uppCons(s):
    s_nova = s.upper()
    i = 0
    while i < len(s):
        if s_nova[i] =='A':          
            s_nova = s_nova.replace('A','a')
        elif s_nova[i]=='E':
            s_nova = s_nova.replace('E','e')
        elif 'I' == s_nova[i]:
            s_nova = s_nova.replace('I','i')
        elif 'O' == s_nova[i]:
            s_nova = s_nova.replace('O','o')
        elif 'U' == s_nova[i]:
            s_nova = s_nova.replace('U','u')
        elif 'Ã' == s_nova[i]:
            s_nova = s_nova.replace('Ã','ã')
        elif 'Ú' == s_nova[i]:
            s_nova = s_nova.replace('Ú', 'ú')
        elif 'Í' == s_nova[i]:
            s_nova = s_nova.replace('Í','í')
        elif 'É' == s_nova[i]:
            s_nova = s_nova.replace('É','é')
        elif 'Ó' == s_nova[i]:
            s_nova = s_nova.replace('Ó', 'ó')
        i = i + 1
    return s_nova