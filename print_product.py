# Usage: print_product.py num1 num2 outfile this is the unicorn branch main
import sys
num1=float(sys.argv[1])
num2=float(sys.argv[2])
fout=open(sys.argv[3],āwā)
fout.write(str(num1*num2)+ā\nā)
