import numpy as np


class Substance:
    def __init__(self, conc, pK=[], vol=100):
        self.conc = conc
        self.K = np.power(10., -np.array(pK))
        self.len_K = len(pK) if pK else 1
        self.vol = vol


class Acid(Substance):
    ...


class Base(Substance):
    ...


def F(X, K):

    den = [X ** (len(K) - i) * np.prod(K[:i]) for i in range(len(K) + 1)]
    num = [i * alpha for i, alpha in enumerate(den)]

    div = np.sum(num, axis=0) / np.sum(den, axis=0)

    return div if K.size else 1


def ion(sample: Substance, titrant: Substance):

    # this case is for acid-base titration
    # must generalize for other types of titration

    scale = np.linspace(0, 14, 100_000)

    H = np.power(10, -scale)
    OH = 1e-14 / H

    s = H if isinstance(sample, Acid) else OH
    t = H if isinstance(titrant, Acid) else OH

    return s, t, scale


def titrate(sample: Substance, titrant: Substance):

    sample_ion, titrant_ion, scale = ion(sample, titrant)

    s = F(sample_ion, sample.K)
    t = F(titrant_ion, titrant.K)
    d = sample_ion - titrant_ion

    phi = (s - d / sample.conc) / (t + d / titrant.conc)

    phi[phi <= 0] = np.nan
    phi[phi > (sample.len_K + titrant.len_K)] = np.nan

    return phi, scale


def derivative(y, x):

    dy = np.diff(y) / np.diff(x)
    dx = [(x[i + 1] + x[i]) / 2 for i in range(len(dy))]

    return dy, dx

def main():
    pass


if __name__ == '__main__':
    main()