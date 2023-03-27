# Torque Spec Calculator
 Calculates Torque for FSAE CSUN using ArgParse user interface.

 **Torque Calculations:**<br>
 python ts_fsae.py -s [insert Screw size] -t [insert Threads/in.] -k [insert Torque Factor] -[np or p]

 s: Screw Diameter<br>
 t: The number of threads<br>
 k: Torque Factor<br>
 np: Non-Permanent<br>
 p: Permanent<br>


 **test examples:**<br>
 python ts_fsae.py -s 0.250 -t 28 -k 0.12 -np<br>
 python ts_fsae.py -s 0.060 -t 80 -k 0.2 -p<br>
 python ts_fsae.py -s 0.500 -t 13 -k 0.2 -np

 **NOTE:**<br>
 Screw dia and Threads/in. must be EXACTLY stated from<br>
 Table 4 and Table 5 from astm_a574 document<br>
 *most are 3 decimal places and some are 4<br>

 **for HELP:**<br>
 python ts_fsae.py -h

# About
Made by Theresa Lee<br>
Last Update: 3/26/2023<br>
Version: Python 3.10.4

DO_NOT_TOUCH.txt data pulled from<br>
*'Standard Specification for Alloy Steel Socket-Head Cap Screws'* by ASTM
