from Bio import SeqIO

def parse_fasta(input_file, output_file):
    with open(input_file, "r") as fasta, open(output_file, "w") as out:
        for record in SeqIO.parse(fasta, "fasta"):
            out.write(f">{record.id}\n")
            out.write(f"{record.seq}\n")

parse_fasta(snakemake.input[0], snakemake.output[0])
