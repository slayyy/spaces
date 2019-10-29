import argparse
import os

parser = argparse.ArgumentParser(description="Rename file")
group = parser.add_mutually_exclusive_group()

parser.add_argument("file", help="taking filename", type=str, nargs='+')

group.add_argument("-s", "--space", action="store_true")
group.add_argument("-r", "--recursive", action="store_true")

args = parser.parse_args()

new_filename = '_'.join(args.file)

filename = ' '.join(args.file)

if args.space:
    new_filename = args.file[0].replace('_', ' ')
elif args.recursive:
    for file in args.file:
        os.rename(file, file.replace(' ', '_'))
else:
    os.rename(filename, new_filename)