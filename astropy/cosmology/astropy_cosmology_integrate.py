#!/usr/bin/env python

from __future__ import division, print_function


import numpy as np

import astropy.cosmology

cosmo = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=0.3)
cosmo_EdS = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=1)
cosmo_dS = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=0)
cosmo_closed = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=1.5)

# Force use of elliptic versions
for c in cosmo, cosmo_EdS, cosmo_dS, cosmo_closed:
    c._comoving_distance_z1z2 = c._integrate_comoving_distance_z1z2


def run_comoving_distance(cos, n=10000, z_max=10.0):
    z = (z_max/n) * np.arange(n) + 0.001
    return z, cos.comoving_distance(z)
