#!/usr/bin/env python

"""Benchmark the standard vs. elliptic form of FlatLCDM."""

import timeit


def run_bench(kind):
    module_name = "astropy_cosmology"
    if kind:
        module_name += '_%s' % kind

    z_max = 100
    setup_commands = 'import %s as ac' % module_name

    repeat = 1000
    n = 2000

    def time_cos(object_name):
        return timeit.timeit(
            'ac.run_comoving_distance(%s, %d, z_max=%f)' %
            (object_name, n, z_max),
            setup=setup_commands, number=repeat)

    general_result = time_cos("ac.cosmo")
    EdS_result = time_cos("ac.cosmo_EdS")
    dS_result = time_cos("ac.cosmo_dS")

    print(kind.upper())
    print("Time to calculate comoving distance for %d redshifts." % n)
    result_names = ((general_result, "General"),
                    (EdS_result, "Einstein - de Sitter"),
                    (dS_result, "de Sitter"))
    for result, name in result_names:
        print("%30s : %.3g s" % (name, float(result)/float(repeat)))


if __name__ == "__main__":
    run_bench("elliptic")
    run_bench("hypergeometric")
    run_bench("integrate")
