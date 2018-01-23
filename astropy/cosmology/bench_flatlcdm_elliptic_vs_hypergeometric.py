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

    # Include z_max, repeat, n by closure
    def time_cos(object_name):
        return timeit.timeit(
            'ac.run_comoving_distance(%s, %d, z_max=%f)' %
            (object_name, n, z_max),
            setup=setup_commands, number=repeat)

    print(kind.upper())
    print("Time to calculate comoving distance for %d redshifts." % n)
    result_cos_names = (("cosmo", "General"),
                        ("cosmo_EdS", "Einstein - de Sitter"),
                        ("cosmo_dS", "de Sitter"))

    for cos, name in result_cos_names:
        result = time_cos("ac.%s" % cos)
        print("%30s : %.3g s" % (name, float(result)/float(repeat)))


if __name__ == "__main__":
    run_bench("integral")
    run_bench("hypergeometric")
