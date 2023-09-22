def pontos_por_time(t):
    r0=t[0][2][0]
    r1=t[1][2][1]
    s0=t[0][2][1]
    s1=t[1][2][0]
    if r0>s0 and r1>s1:
        v={t[0][1]: 6,t[1][0]: 0}
        return v
    if r0>s0 and r1<s1:
        v={t[0][0]: 4,t[1][0]: 1}
        return v
    if r0<s0 and r1<s1:
        v={t[0][0]: 0,t[1][0]: 6}
        return v
    if r0<s0 and r1>s1:
        v={t[0][0]: 1,t[1][0]: 4}
        return v
    if r0==s0 and r1==s1:
        v={t[0][0]: 2,t[1][0]: 2}
        return v