# omicR_for_RStudio

omicR creates fasta files, downloads genomes from NCBI using the refseq number, creates databases to run BLAST+, runs BLAST+ and filters these results to obtain the best match per sequence. 
These scripts can be used to run BLAST alignment of short-read (DArTseq data) and long-read sequences (Illumina, PacBio… etc). You can use reference genomes from NCBI, genomes from your private collection, contigs, scaffolds or any other genetic sequence that you would like to use as reference. 

watch the tutorial video in YouTube
omicR in R Studio (~20 min)
https://youtu.be/2dEgOBjcvM8 

1)	You need to install the following:

a.	Python V3 or latest: https://www.python.org/downloads/

b.	Biopython https://biopython.org/

c.	Download the omicR project. This should include at least the following:  “omicR.Rproj”, “TestingPyCharm_MKfasta.py”,  “TestingPyCharm_Downloading_genomes.py”, “TestingPyCharm_MakeDataBase.py”, “TestingPyCharm_BLAST_filtering_and_all.py”, “TestingPyCharm_NCBI_BLAST_filtering.py”

d.	BLAST+ latest version: https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
