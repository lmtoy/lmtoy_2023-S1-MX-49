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
pars1["L1157-B1"] = ""


#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["L1157-B1"] = "pix_list=-13"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)
