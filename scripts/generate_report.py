from jinja2 import Template
import pandas as pd

def generate_html_report(fasta, blast, alignment, output_file):
    template = """
    <html>
    <head><title>Bioinformatics Pipeline Report</title></head>
    <body>
        <h1>Pipeline Report</h1>
        <h2>Parsed Sequences</h2>
        <pre>{{ fasta_content }}</pre>
        
        <h2>BLAST Results</h2>
        <pre>{{ blast_content }}</pre>
        
        <h2>ClustalW Alignment</h2>
        <pre>{{ alignment_content }}</pre>
    </body>
    </html>
    """
    with open(fasta, "r") as f:
        fasta_content = f.read()
    with open(blast, "r") as b:
        blast_content = b.read()
    with open(alignment, "r") as a:
        alignment_content = a.read()

    html_content = Template(template).render(
        fasta_content=fasta_content,
        blast_content=blast_content,
        alignment_content=alignment_content,
    )
    with open(output_file, "w") as out:
        out.write(html_content)

generate_html_report(
    snakemake.input.fasta,
    snakemake.input.blast,
    snakemake.input.alignment,
    snakemake.output[0]
)
