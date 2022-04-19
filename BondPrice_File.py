

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    pvcfsum = 0
    cf = face * couponRate/ppy
    
    for t in range(1,(m*ppy) + 1):
        pv = (1 + (y/ppy))**(-t)
        pvcf = pv * cf
        pvcfsum = pvcfsum + pvcf
    
    pvcfsum = pvcfsum + face * pv
    return pvcfsum
    


