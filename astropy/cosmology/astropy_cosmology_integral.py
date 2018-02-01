#!/usr/bin/env python

from __future__ import division, print_function


import numpy as np

import astropy.cosmology

cosmo_flat = astropy.cosmology.LambdaCDM(H0=70, Om0=0.3, Ode0=0.7)
cosmo_EdS = astropy.cosmology.LambdaCDM(H0=70, Om0=1, Ode0=0)
cosmo_dS = astropy.cosmology.LambdaCDM(H0=70, Om0=0, Ode0=1)
cosmo_closed_flat = astropy.cosmology.LambdaCDM(H0=70, Om0=1.5, Ode0=-0.5)
cosmo_closed_nonflat = astropy.cosmology.LambdaCDM(H0=70, Om0=1.5, Ode0=0.3)
cosmo_open_nonflat = astropy.cosmology.LambdaCDM(H0=70, Om0=0.5, Ode0=0.2)

# Force use of elliptic versions in the cosmology objects
cosmologies = (cosmo_flat, cosmo_EdS, cosmo_dS,
               cosmo_closed_flat, cosmo_closed_nonflat, cosmo_open_nonflat)
for c in cosmologies:
    c._comoving_distance_z1z2 = c._integral_comoving_distance_z1z2


def run_comoving_distance(cos, n=10000, z_max=10.0):
    z = (z_max/n) * np.arange(n) + 0.001
    return z, cos.comoving_distance(z)
