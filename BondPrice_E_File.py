def getBondPrice_E(face, couponRate, yc):
    bondPrice = 0.0
    coupon = face * couponRate
    m = len(yc)
    for idx, y in enumerate(yc):
        t = idx + 1

        if t < m:
            cf = coupon
        else:
            cf = coupon + face

        pv = 1 / (1 + y) ** t
        bondPrice += cf * pv

    return bondPrice
