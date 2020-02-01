#!/usr/bin/python3

import sys
import argparse
import csv

import matplotlib

matplotlib.use('Agg')

import pylab


TOTAL_FULLGC_TIME = "FGCT"


def parse_argument(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--input-gclog', dest="input_gclog", default='../logs/jstat-gc.log')
    parser.add_argument('--output-dir', dest="output_dir", default='.')

    return parser.parse_args()


def mk_fullgc_graph(input_gclog, output_dir):
    pre_fullgc_time = 0
    fullgc_time_list = []
    with open(input_gclog, "r") as f:
        rows = csv.DictReader(f, delimiter=" ", skipinitialspace=True)
        for row in rows:
            fullgc_time = float(row[TOTAL_FULLGC_TIME])
            fullgc_time_list.append(fullgc_time - pre_fullgc_time)
            pre_fullgc_time = fullgc_time

    pylab.title("Full GC Time(sec)")
    pylab.bar(range(1, len(fullgc_time_list)+1), fullgc_time_list)
    pylab.ylim(0, max(fullgc_time_list))
    pylab.grid(True)
    pylab.savefig("{}/fullgc.png".format(output_dir))
    pylab.close()

def main(argv):
    args = parse_argument(argv)
    mk_fullgc_graph(args.input_gclog, args.output_dir)

if __name__ == '__main__':
    main(sys.argv[:1])

