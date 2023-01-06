from math import log2

# IRS = 0.273758 * TMB + 0.112641 * PD-1 + 0.061904 * PD-L1 - 0.077011 * TOP2A - 0.057991 * ADAM12

COEFS = [
    0.273758315,
    0.112641273,
    0.061903666,
    -0.07701051,
    -0.057991178
]


def irs(adam12, pd1, pdl1, top2a, tmb):
    """
    Calculate immune response score as the dot product of provided inputs and model coefficients
    """
    log2tmb = log2(tmb + 1)
    return sum([
        val * coef
        for val, coef in zip(
            [log2tmb, pd1, pdl1, top2a, adam12],
            COEFS
        )
    ])
