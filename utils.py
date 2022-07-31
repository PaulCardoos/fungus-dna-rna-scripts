import csv 
import os


def read_csv(filepath: str) -> list:
    with open(filepath, "r") as reader:
        return list(csv.DictReader(reader))

def organize_data(data : list) -> dict: 
    """
    organize data by amino acid
    """
    amino_acids = {}

    for row in data:
        if row["AA"] in amino_acids: 
            amino_acids[row["AA"]].append({"DNA" : row["DNA"], "freq" : float(row["Frequency_per_thousand"])})
        else:
            amino_acids[row["AA"]] = [{"DNA" : row["DNA"], "freq" : float(row["Frequency_per_thousand"])}]
    
    return amino_acids

def sort_dict_vals(amino_acids : dict) -> dict:
    """
    Sort entry of the dictionary from highest freq per thousand -> lowest
    """
    return {
        key : sorted(entry, key=lambda x : x["freq"], reverse=True)
        for key, entry in amino_acids.items()
    }

def convert(sequence : str, amino_acids : dict) -> str:
    """
    Takes in a sequence and outputs the optimized sequenece
    """
    i = 0
    j = 3

    new_seq = ""

    while(j <= len(sequence)):
        dna = sequence[i:j]

        for k, v in amino_acids.items():
            for dic in v:
                if dna == dic["DNA"]:
                    
                    aa = k
                    new_seq += amino_acids[aa][0]["DNA"]
                    i += 3
                    j += 3
  
    return new_seq
   
def save_sequence(sequence : str, filename : str):
    if not os.path.isdir("results"):
        os.mkdir("results")
    
    with open(f"results/{filename}", "w") as f:
        f.write(sequence)

    