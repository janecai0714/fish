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
    
def read_pred(filename):
	f = open(filename, "r")
	pred = f.readlines()
	return pred


amp_file_path = "/home/jianxiu/Documents/fish/analGland/AnalGland1DS/"
att_pred_path = "/home/jianxiu/Documents/fish/analGland/AnalGland1DS_att_pred/"

amp_file_list = os.listdir(amp_file_path)
amp_file_list.sort()
att_pred_list = os.listdir(att_pred_path)
att_pred_list.sort()

whole_seq_name_list = []
whole_seq_list = []
whole_att_list = []
for i in range(len(amp_file_list)):
	seq_file_path = amp_file_path + amp_file_list[i]
	seq_dict = read_fasta_file(seq_file_path)
	for key, value in seq_dict.items():
		whole_seq_name_list.append(key)
		whole_seq_list.append(value)
	
	att_file_path = att_pred_path + att_pred_list[i]
	att_list = read_pred(att_file_path)
	for j in range(len(att_list)):
		whole_att_list.append(att_list[j])

seq_pred_file = open("/home/jianxiu/Documents/fish/seq_pred.csv", "w")
csvwriter = csv.writer(seq_pred_file)
header = ["seq_name", "seq", "att_pred"]
csvwriter.writerow(header)

for i in range(len(whole_seq_name_list)):
	one_row = []
	one_row.append(whole_seq_name_list[i])
	one_row.append(whole_seq_list[i])
	one_row.append(whole_att_list[i])
	csvwriter.writerow(one_row)
seq_pred_file.close()
