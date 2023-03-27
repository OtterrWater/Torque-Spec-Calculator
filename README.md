# Torque Spec Calculator
 Calculates Torque for FSAE CSUN using ArgParse user interface.

 Torque Calculations:
 python ts_fsae.py -s [insert Screw size] -t [insert Threads/in.] -k [insert Torque Factor] -[np or p]

 s: Screw Diameter`<br>`
 t: The number of threads
 k: Torque Factor
 np: Non-Permanent
 p: Permanent


 test examples:
 python ts_fsae.py -s 0.250 -t 28 -k 0.12 -np
 python ts_fsae.py -s 0.060 -t 80 -k 0.2 -p
 python ts_fsae.py -s 0.500 -t 13 -k 0.2 -np

 NOTE:
 Screw dia and Threads/in. must be EXACTLY stated from
 Table 4 and Table 5 from astm_a574 document
 *most are 3 decimal places and some are 4

 for HELP:
 python ts_fsae.py -h

Made by Theresa Lee
Last Update: 3/26/2023
Version: Python 3.10.4


DO_NOT_TOUCH.txt data pulled from
'Standard Specification for Alloy Steel Socket-Head Cap Screws' by ASTM
