seq = "ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"

import re
GTGTGT=re.findall(r"GTGTGT",seq)
GTCTGT=re.findall(r"GTCTGT",seq)
total_rep=int(len(GTGTGT))+int(len(GTCTGT))
print("the total number of repeat elements is",total_rep)
