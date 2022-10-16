import random

def read_fasta_file(filename):
    f = open(filename, "r")
    seq = {}
    for line in f:
        if line.startswith(">"):
            name = line.split()[0]
            seq[name] = ''
        else:
            seq[name] += line.replace("\n", '').strip()
    f.close()
    return seq

def shuffle_fasta_file(seq, out_file_name):
    random.seed(1234)
    randomrized_file = open(out_file_name, 'w')
    for key, value in seq.items():
        randomrized_file.writelines(key + '\n')
        value = ''.join(random.sample(value, len(value)))
        randomrized_file.writelines(value + '\n')
    randomrized_file.close()

in_file_name = 'E:/fish/extracted_ORFs/AnalFin1DS_input.fasta' # set the name of input file
out_file_name = "E:/fish/randomrized_files/AnalFin1DS_input_randomrized.fasta" # set the name of output file

seq = read_fasta_file(in_file_name)
shuffle_fasta_file(seq, out_file_name)