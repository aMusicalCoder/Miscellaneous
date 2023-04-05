"""
ID: ben.wag1
LANG: PYTHON3
PROG: beads
"""

import os

#open io streams
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

n_beads = int(fin.readline())
beads = fin.readline()

maxBeads = 0

for breakPoint in range(n_beads):
    #first transform string to start on breakPoint character
    end = ""
    newBeads = ""
    beadCount = 0
    for i in range(n_beads):
        if(i < breakPoint):
            end = end + beads[i]
        else:
            newBeads = newBeads + beads[i]
    
    newBeads = newBeads + end

    fwdColorChange = False
    bwdColorChange = False

    if(newBeads[0] == 'w'):
        beadCount = beadCount + 1
    
    if(newBeads[n_beads - 1] == 'w'):
        beadCount = beadCount + 1

    if((newBeads[0] == 'w' and newBeads[n_beads - 1] != 'w') or (newBeads[n_beads - 1] == 'w' and newBeads[0] != 'w')):
        beadCount = beadCount + 1

    for i in range(n_beads):
        if(not fwdColorChange):
            if(newBeads[0] == newBeads[i] or newBeads[i] == 'w'):
                beadCount = beadCount + 1
            else:
                fwdColorChange = True
        if(not bwdColorChange):
            if(newBeads[n_beads - 1] == newBeads[n_beads - (i+1)] or newBeads[n_beads - (i+1)] == 'w'):
                beadCount = beadCount + 1
            else:
                bwdColorChange = True
    
    #edge cases
    if(beadCount >= n_beads):
        beadCount = n_beads
    
    if(beadCount >= maxBeads):
        maxBeads = beadCount

fout.write(f'{maxBeads}\n')
print(maxBeads)

fin.close()
fout.close()