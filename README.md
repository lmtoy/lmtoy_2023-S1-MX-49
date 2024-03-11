# 2023-S1-MX-49



this project was observed with two banks,at 87.88 and 95.936 GHz at intermediate (400MHz) band, 4096 channels.

The default reduction is with dv=20, dw=20, but an initial run was made as __wide, with a very wide dv=100 dw=600, to show the 
large number of birdies, and absense of any obvious signal


bank 0 has a strong birdie in beam 5,12,13,  they also seem to add noise to the off-birdie channels nearby, at least in beams 5,13

bank 1 needs beam 0 to be removed, pipeline crashes when used. beams 4,5,8,9 have birdies at 2048. beams 2,14 at 2045,2048,2051,
i.e. with the strong wings

bank=0
  X       Y       Ypeak    Delta    Delta
  delta=0.0220529
2048.000000 1.540490  0.391545 0.391630 0.391459

bank=1
  X       Y       Ypeak    Delta    Delta
  delta=0.0298767
2045.000000 1.840541  0.501263 0.499628 0.502898
2048.000000 3.097673  1.758578 1.760314 1.756841
2051.000000 1.823601  0.491438 0.489129 0.493747
