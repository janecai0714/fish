import os
import collections
import csv

def read_fasta_file(filename):
    f = open(filename, "r")
    seq = collections.OrderedDict()
    for line in f:
        if line.startswith(">"):
            name = line.split()[0]
            seq[name] = ''
        else:
            seq[name] += line.replace("\n", '').strip()
    f.close()
    return seq
    

seq_file_path = "/home/jianxiu/Documents/analFin/AnalFin1DS/AnalFin1DS_orf_18.fasta"
seq_dict = read_fasta_file(seq_file_path)

leq_150_dict = collections.OrderedDict()
leq_150_file = open("/home/jianxiu/Documents/analFin/AnalFin1DS/AnalFin1DS_orf_18.fasta", "w")
for key, value in seq_dict.items():
	if len(value) <= 150:
		name = key
		leq_150_dict[name] = value
		leq_150_file.write(key+"\n")
		leq_150_file.write(value+"\n")

print(len(leq_150_dict))	
leq_150_file.close()
