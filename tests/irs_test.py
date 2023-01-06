import irs


def test_irs():
    # spot check against reference implementation
    adam12 = -2.04359
    pdcd1 = 1.4943
    pdl1 = 0.543743
    top2a = -0.506425
    tmb = 4.890867076854636
    expected_irs = 1.0599
    calculated_irs = irs.irs(adam12, pdcd1, pdl1, top2a, tmb)
    assert abs(expected_irs - calculated_irs) < 1e-5


if __name__ == "__main__":
    test_irs()
