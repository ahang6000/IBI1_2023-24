#read original fastq file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    lines = f.readlines()
    
import re

#set the variables
gene_name = ''
gene_seq = ''
gene_description=""
duplicate_genes = []

#use for loop to process the fastq file(in the first loop: record the variables; at the begining of the second loop: select the duplicate gene)
for line in lines:
    if line.startswith('>'):
        gene_seq = gene_seq[:-1]
        if 'duplication' in gene_description:
            duplicate_genes.append((gene_name, gene_seq))
        gene_name = re.findall(r" gene:(.+?) ",line)
        gene_name = gene_name[0]
        gene_description = line.strip('>\n').split(' ')
        gene_seq = ''
    else:
        gene_seq += line.strip()
        gene_seq += "\n"
        
#save the duplicate gene in another fastq file
with open('duplicate_genes.fa', 'w') as f:
    for name, seq in duplicate_genes:
        f.write(f'>{name}\n{seq}\n')