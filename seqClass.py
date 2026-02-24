#!/usr/bin/env python

# Import necessary modules
# sys: to handle command-line arguments and exit
# re: to perform regular expression searches
# ArgumentParser: to parse command-line arguments
import sys, re
from argparse import ArgumentParser

# The argument parser with a description of the script
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')

# Add required argument: the input sequence
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# Add extra argument: a motif to search for in the sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# If no arguments are provided, print the help message and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the arguments from the command line
args = parser.parse_args()

# Convert the sequence to uppercase 
args.seq = args.seq.upper()

# Check if the sequence contains only valid nucleotide characters (A, C, G, T, U)
if re.search('^[ACGTU]+$', args.seq):
    # If the sequence contains T, it is DNA
    if re.search('T', args.seq):
        print('The sequence is DNA')
    # If the sequence contains U, it is RNA
    elif re.search('U', args.seq):
        print('The sequence is RNA')
    # If it contains neither T nor U, it could be either
    else:
        print('The sequence can be DNA or RNA')
else:
    # If the sequence contains invalid characters, it is neither DNA nor RNA
    print('The sequence is not DNA nor RNA')

# If a motif was provided, search for it in the sequence
if args.motif:
    # Convert the motif to uppercase 
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    # Search for the motif in the sequence using regex
    if re.search(args.motif, args.seq):
        print("FOUND in motif")
    else:
        print("Motif NOT FOUND in the sequence!")
