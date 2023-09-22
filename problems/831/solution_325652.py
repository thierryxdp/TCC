def lingua_p(palavra):
    x=str.replace(palavra,'a','apa')
    y=str.replace(x,'e','epe')
    z=str.replace(y,'i','ipi')
    v=str.replace(z,'o','opo')
    t=str.replace(v,'u','upu')
    return str.lower(t)