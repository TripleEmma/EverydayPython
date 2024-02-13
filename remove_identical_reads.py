#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:03:35 2024

This script output unique reads (remove identical reads)

@author: Emma
"""

from Bio import SeqIO
import gzip

class input_seq():
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq
    def get_name(self):
        return self.name
    def get_seq(self):
        return self.seq

def read_sequence_file(sequence_file):
    names = []
    sequences = []

    if sequence_file.endswith((".fasta", ".fa", ".fasta.gz", ".fa.gz")):
        file_format = "fasta"
    elif sequence_file.endswith((".fastq", ".fq", ".fastq.gz", ".fq.gz")):
        file_format = "fastq"
    else:
        raise ValueError("Unsupported file format")

    with gzip.open(sequence_file, "rt") if sequence_file.endswith(".gz") else open(sequence_file, "rt") as handle:
        for record in SeqIO.parse(handle, file_format):
            names.append(record.id)
            sequences.append(record.seq[1:50])
    return names, sequences

def build_data(names, sequences):
    seq_data = []
    for i in range(len(names)):
        seq_data.append(input_seq(names[i], sequences[i]))
    return seq_data

def sort_data(seq_data):
    seq_data_copy = sorted(seq_data, key = input_seq.get_seq)
    return seq_data_copy

def cluster(seq_data_copy):
    cluster_seq = []
    seq_n = len(seq_data_copy)
    cluster_seq.append(seq_data_copy[0].get_name())
    i = 0
    while i < seq_n-1:
        for j in range(i+1, seq_n):
            if seq_data_copy[i].get_seq() != seq_data_copy[j].get_seq():
               cluster_seq.append(seq_data_copy[j].get_name())
               i += 1
               break
            else:
               i += 1
    return(cluster_seq)

if __name__ == '__main__':
    import sys
    seq_file = sys.argv[1]
    names, sequences = read_sequence_file(seq_file)
    seq_data = build_data(names, sequences)
    seq_data_copy = sort_data(seq_data)
    cluster_seq = cluster(seq_data_copy)
    print(len(cluster_seq))
