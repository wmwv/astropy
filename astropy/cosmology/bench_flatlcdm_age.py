#!/usr/bin/env python

"""Benchmark the standard vs. elliptic form of FlatLCDM."""

import math
import timeit


def run_bench(kind):
    module_name = "astropy_cosmology"
    if kind:
        module_name += '_%s' % kind

    z_max = 100
    setup_commands = 'import %s as ac' % module_name

    repeat = 100
    n = 200

    # Include z_max, repeat, n by closure
    def time_cos(object_name):
        try:
            r = timeit.timeit(
                'ac.run_age(%s, %d, z_max=%f)' %
                (object_name, n, z_max),
                setup=setup_commands, number=repeat)
        except TypeError as te:
            print("TypeError:", te)
            return math.nan

        return r

    print(kind.upper())
    print("Time to calculate age for %d redshifts." % n)
    result_cos_names = (("cosmo", "General"),
                        ("cosmo_EdS", "Einstein - de Sitter"),
                        ("cosmo_dS", "de Sitter"),
                        ("cosmo_closed", "Omega_M > 1"))

    for cos, name in result_cos_names:
        result = time_cos("ac.%s" % cos)
        print("%30s : %.3g s" % (name, float(result)/float(repeat)))


if __name__ == "__main__":
    run_bench("integral")
    run_bench("analytic")
