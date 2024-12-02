# Specify the final output of the workflow
rule all:
    input:
        "results/report.html"

# Rule to parse a FASTA file
rule parse_fasta:
    input:
        "data/sequences.fasta"
    output:
        "results/parsed_sequences.txt"
    script:
        "scripts/parse_fasta.py"

# Rule to run BLAST
rule run_blast:
    input:
        "data/sequences.fasta"
    output:
        "results/blast_results.txt"
    shell:
        "blastn -query {input} -db nt -out {output}"

# Rule to perform sequence alignment with ClustalW
rule clustalw_alignment:
    input:
        "data/sequences.fasta"
    output:
        "results/alignment.aln"
    shell:
        "clustalo -i {input} -o {output} --outfmt=fa"


# Rule to generate an HTML report
rule generate_report:
    input:
        fasta="results/parsed_sequences.txt",
        blast="results/blast_results.txt",
        alignment="results/alignment.aln"
    output:
        "results/report.html"
    script:
        "scripts/generate_report.py"
