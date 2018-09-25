#!/usr/bin/env python
import json, sys, os
from urllib import urlopen

SERVER="http://aflowlib.duke.edu"
API="/search/API/?"
MATCHBOOK="species((Na:K),Cl),nspecies(2),Egap(2*,*5),energy_cell"
DIRECTIVES="$paging(0)"
SUMMONS=MATCHBOOK+","+DIRECTIVES

response=json.loads(urlopen(SERVER+API+SUMMONS).read().decode("utf-8"))
for datum in response:
    bandgap=[float(x) for x in datum['Egap'].split(",")]
    energycell=[float(x) for x in datum['energy_cell'].split(",")]    
    print ("{}, {}, {}".format( datum['auid'], bandgap, energycell))
