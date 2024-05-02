#read original fastq file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    lines = f.readlines()

import re

#set the variables
gene_name = ''
gene_seq = ''
gene_description=""
duplicate_genes = []

dp=input("Please enter duplicate sequences: ")


if dp=="GTCTGT":
#use for loop to process the fastq file(in the first loop: record the variables; at the begining of the second loop: select the duplicate gene)
 for line in lines:
    if line.startswith('>'):
        if 'duplication' in gene_description:
            #count the GTGTGT
            GTCTGT=re.findall(r"GTCTGT",gene_seq)
            gene_name +="  GTCTGT number: "
            gene_name += str(len(GTCTGT))
            duplicate_genes.append((gene_name, gene_seq))
        gene_name = re.findall(r" gene:(.+?) ",line)
        gene_name = gene_name[0]
        gene_description = line.strip('>\n').split(' ')
        gene_seq = ''
    else:
        gene_seq += line.strip()
        
#save the duplicate gene in another fastq file
 with open('GTCTGT_duplicate_genes.fa', 'w') as f:
    for name, seq in duplicate_genes:
        f.write(f'>{name}\n{seq}\n')
        

elif dp=="GTGTGT":
#use for loop to process the fastq file(in the first loop: record the variables; at the begining of the second loop: select the duplicate gene)
 for line in lines:
    if line.startswith('>'):
        if 'duplication' in gene_description:
            #count the GTGTGT
            GTGTGT=re.findall(r"GTGTGT",gene_seq)
            gene_name +="  GTGTGT number: "
            gene_name += str(len(GTGTGT))
            duplicate_genes.append((gene_name, gene_seq))
        gene_name = re.findall(r" gene:(.+?) ",line)
        gene_name = gene_name[0]
        gene_description = line.strip('>\n').split(' ')
        gene_seq = ''
    else:
        gene_seq += line.strip()
        
#save the duplicate gene in another fastq file
 with open('GTGTGT_duplicate_genes.fa', 'w') as f:
    for name, seq in duplicate_genes:
        f.write(f'>{name}\n{seq}\n')
        
else:
    print("Please enter the correct sequence!")
