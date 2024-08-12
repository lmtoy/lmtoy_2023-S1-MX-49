#! /usr/bin/env python
#

import os
import sys
from lmtoy import runs

project="2023-S1-MX-49"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["L1157-B1"] =  [ 109989, 109990,]                                        # may 8

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["L1157-B1"] = "extent=200 dv=20 dw=20 pix_list=-0"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["L1157-B1"] = "bank=0 pix_list=-5,12,13"

#        common parameters per source on subsequent runs (run1c, run2c)
pars3 = {}
pars3["L1157-B1"] = "bank=1 pix_list=-0,2,3,4,8,9,14,15"

#        or this
pars2_test = ["oid=0 bank=0 pix_list=-5,12,13",
              "oid=1 bank=1 pix_list=-0,2,3,4,8,9,14,15"]

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, argv=sys.argv)
