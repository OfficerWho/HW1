
def getBondDuration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    cf = face * couponRate
    wsum = 0
    pv = 0

    for t in range(1,(m*ppy + 1)):
        pv = (1 + y)**-t
        pvcf = pv * cf
        pvcfsum = pvcfsum + pvcf
        w = pvcf * t
        wsum = wsum + w
    pvcfsum = pvcfsum + face * pv
    wsum = wsum + face * pv * t

    duration = wsum/pvcfsum
    return duration

