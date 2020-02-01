#!/usr/bin/python3

import sys
import argparse
import csv

import matplotlib

matplotlib.use('Agg')

import pylab


EDEN_USED = "EU"
META_USED = "MU"
COMPRESSED_CLASS_SPCE_USE = "CCSU"
SUVERIVOR_0_USED = "S0U"
SUVERIVOR_1_USED = "S1U"
OLD_USED = "OU"


def parse_argument(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--input-gclog', dest="input_gclog", default='../logs/jstat-gc.log')
    parser.add_argument('--output-dir', dest="output_dir", default='.')

    return parser.parse_args()


def mk_fullgc_graph(input_gclog, output_dir):
    yang_used_list = []
    old_used_list = []
    eden_used_list = []
    meta_used_list = []
    compressed_class_space_used_list = []
    with open(input_gclog, "r") as f:
        rows = csv.DictReader(f, delimiter=" ", skipinitialspace=True)
        for row in rows:
            yang_used_list.append(float(row[SUVERIVOR_0_USED]) + float(row[SUVERIVOR_1_USED]))
            old_used_list.append(float(row[OLD_USED]))
            eden_used_list.append(float(row[EDEN_USED]))
            meta_used_list.append(float(row[META_USED]))
            compressed_class_space_used_list.append(float(row[COMPRESSED_CLASS_SPCE_USE]))


    labels = [ "Eden", "Meta", "Compress Class", "Yang", "Old" ]
    data_list = [ eden_used_list, meta_used_list, compressed_class_space_used_list, yang_used_list, old_used_list ]
    index_list = range(1, len(old_used_list)+1)

    pylab.stackplot(index_list, data_list, labels=labels)
    pylab.title("Heap Size(KB)")
    pylab.grid(True)
    pylab.legend(loc='upper right')
    pylab.savefig("{}/heapsize.png".format(output_dir))
    pylab.close()

def main(argv):
    args = parse_argument(argv)
    mk_fullgc_graph(args.input_gclog, args.output_dir)

if __name__ == '__main__':
    main(sys.argv[:1])

