def pontos_por_time[[[x,y],[a,b]],[[x,y],[c,d]]]:
    px()
    py()
    if a>b:
        px = px + (3)
        if a<b:
            py = px +(3)
            if a==b:
                px = px +(1) and py = py +(1)
                if c>d:
                    px= px +(3)
                    if c<d:
                        py= py +(3)
                        if c==d:
                            px = px+(1) and py= py+(1)
                            return {x:px,y:py}