#Made by Theresa Lee
#Date: 3/26/2023
#Version: Python 3.10.4

#HOW TO USE:--------------------------------------------------------------------------------------------------
'''

Torque Calculations:
python ts_fsae.py -s [insert Screw size] -t [insert Threads/in.] -k [insert Torque Factor] -[np or p]

s: Screw Diameter
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
'''

#HOW TO DOWNLOAD LIBRARY-----------------------------------------------------------------------------------------
'''INPUT INTO TERMINAL
Pandas:
pip install pandas

ArgParse:
pip install argparse

'''

#-----------------------------------------------------------------------------------------------------------------
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Orgamize files')
#screw dia and threads
parser.add_argument('-s','--screw_dia',metavar=' ', required='true',help='The diameter Screw')
parser.add_argument('-t','--threads',metavar=' ', required='true',help='The number of Threads/in.')
parser.add_argument('-k','--T_factor',metavar=' ', required='true',help='k is Torque Factor')

parser.add_argument('-np','--non_perm', action ='store_true', help = 'Uses Non-Permanent Fi')
parser.add_argument('-p','--perm', action ='store_true', help = 'Uses Permanent Fi')
args = parser.parse_args()

data = []
with open("DO_NOT_TOUCH.txt", "r") as f:
    for ln in f:
        ln = ln.strip()
        if not ln:
            continue
        parts = ln.split()
        data_nums = parts[:5]
        data.append(data_nums)
f.close()

coarse = pd.DataFrame(data, columns=['Screw Dia(D), in.', 'Threads/in.', 'Tensile Load, min, lbf^A', 'Stress Area, in.^2B', 'Proof Load(Length Measurement Method), min, lbf C']).iloc[:31]
fine = pd.DataFrame(data, columns=['Screw Dia(D), in.', 'Threads/in.', 'Tensile Load, min, lbf^A', 'Stress Area, in.^2B', 'Proof Load(Length Measurement Method), min, lbf C']).iloc[31:]

print('---------------------------------------------------------------')
for i, row in coarse.iterrows():
    if row['Screw Dia(D), in.'] == args.screw_dia and row['Threads/in.'] == args.threads:
        coarse_d = row['Screw Dia(D), in.']
        coarse_pf = row['Proof Load(Length Measurement Method), min, lbf C']
        print('Tensile Requirements for Coarse Thread Screws:\n', row.to_string(index=True))
    else:
        continue

for i, row in fine.iterrows():
    if row['Screw Dia(D), in.'] == args.screw_dia and row['Threads/in.'] == args.threads:
        fine_d = row['Screw Dia(D), in.']
        fine_pf = row['Proof Load(Length Measurement Method), min, lbf C']
        print('Tensile Requirements for Fine Thread Screws:\n',row.to_string(index=True))
    else:
        continue


print('\n---------------------------------------------------------------')
def Fi(c, fp):
    Fi = float(c)*float(fp)
    return Fi

print('Torque Calculations:')
if __name__ == '__main__':
    k = float(args.T_factor)
    c_non_perm = 0.75
    c_perm = 0.9

    if args.non_perm:
        if 'coarse_d' in locals() or 'coarse_d' in globals():
            Fi_non_perm = float(c_non_perm) * float(coarse_pf)
            T=k*Fi_non_perm*float(coarse_d)
            print('Non-Permanent Fi = %s * %s' % (c_non_perm, coarse_pf))
            print('Fi =', Fi_non_perm, 'lbf')
            print('T = (%s*%s*%s)/12' % (k,Fi_non_perm,coarse_d))
            print('T =',T/12, 'ft.lbf')
        else:
            pass

        if 'fine_d' in locals() or 'fine_d' in globals():
            Fi_non_perm = float(c_non_perm) * float(fine_pf)
            T=k*Fi_non_perm*float(fine_d)
            print('Non-Permanent Fi = %s * %s' % (c_non_perm, fine_pf))
            print('Fi =', Fi_non_perm, 'lbf')
            print('T = (%s*%s*%s)/12' % (k,Fi_non_perm,fine_d))
            print('T =',T/12, 'ft.lbf')
        else:
            exit()

    elif args.perm:
        if 'coarse_d' in locals() or 'coarse_d' in globals():
            Fi_perm = float(c_perm) * float(coarse_pf)
            T=k*Fi_perm*float(coarse_d)
            print('Non-Permanent Fi = %s * %s' % (c_perm, coarse_pf))
            print('Fi =', Fi_perm, 'lbf')
            print('T = (%s*%s*%s)/12' % (k,Fi_perm,coarse_d))
            print('T =',T/12, 'ft.lbf')
        else:
            pass

        if 'fine_d' in locals() or 'fine_d' in globals():
            Fi_perm = float(c_perm) * float(fine_pf)
            T=k*Fi_perm*float(fine_d)
            print('Non-Permanent Fi = %s * %s' % (c_perm, fine_pf))
            print('Fi =', Fi_perm, 'lbf')
            print('T = (%s*%s*%s)/12' % (k,Fi_perm,fine_d))
            print('T =',T/12, 'ft.lbf')
        else:
            exit()

    else:
        print('argument Permanent or Non-Permanent is missing')
print('---------------------------------------------------------------')