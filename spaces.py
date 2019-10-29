import argparse
import os

parser = argparse.ArgumentParser(description="squaring number")
group = parser.add_mutually_exclusive_group()

parser.add_argument("file", help="taking filename", type=str, nargs='+')
parser.add_argument("filename", help="taking filename", type=str)

group.add_argument("-space", "--space", action="store_true")

args = parser.parse_args()

new_filename = '_'.join(args.file)

filename = ' '.join(args.file)

if args.space:
    new_filename = args.file[0].replace('_', ' ')

# os.rename(filename, new_filename)
print(vars(args))