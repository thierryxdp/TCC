if s1j1==s2j1:
        if s1j2==s2j2:
            p1=2
            p2=2
        if s1j2>s2j2:
            p1=4
            p2=1
        if s1j2<s2j2:
            p1=1
            p=4
    if s1j2==s2j2:
        if s1j1>s2j1:
            p1=4
            p2=1
        if s1j1<s2j1:
            p1=1
            p=4
    if s1j1>s2j1:
        if s1j2>s2j2:
            p1=6
            p2=0
        if s1j2<s2j2:
            p1=3
            p2=3
    if s1j1<s2j1:
        if s1j2>s2j2:
            p1=3
            p2=3
        if s1j2<s2j2:
            p1=0
            p2=6
    return {t1:p1,t2:p2}