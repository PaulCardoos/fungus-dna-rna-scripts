from utils import read_csv, organize_data, sort_dict_vals, convert, save_sequence
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--seq", help="enter the name of the output file")
    parser.add_argument("--output", help="enter the name of the output file")
    args = parser.parse_args()

    some_data = read_csv("/Users/mirna/fungus-code/fungus.csv")
    aa = organize_data(some_data)
    aa = sort_dict_vals(aa)
    sequence = convert(args.seq, aa)
    save_sequence(sequence, args.output)
main()