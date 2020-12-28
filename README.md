# omicR_for_RStudio

omicR creates fasta files, downloads genomes from NCBI using the refseq number, creates databases to run BLAST+, runs BLAST+ and filters these results to obtain the best match per sequence. 
These scripts can be used to run BLAST alignment of short-read (DArTseq data) and long-read sequences (Illumina, PacBio… etc). You can use reference genomes from NCBI, genomes from your private collection, contigs, scaffolds or any other genetic sequence that you would like to use as reference. 



1)	You need to install the following:

a.	Python V3 or latest: https://www.python.org/downloads/

b.	Biopython https://biopython.org/

c.	Download the omicR project. This should include at least the following:  “omicR.Rproj”, “mkfastafile.R”, “downloadGenomes.R”,” makeDatabase.R”, “BLASTnFilter.R”, “filter.R” , “TestingPyCharm_MKfasta.py”,  “TestingPyCharm_Downloading_genomes.py”, “TestingPyCharm_MakeDataBase.py”, “TestingPyCharm_BLAST_filtering_and_all.py”, “TestingPyCharm_NCBI_BLAST_filtering.py”

d.	BLAST+ latest version: https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/






INSTRUCTIONS 

*Download and unzip the files from GitHub.

*Open the project omicR.Rproj

*Go to the section BUILD (Top right of the window) and click "Install and Restart"

*You can open the scripts as you click on them in the section "Files" (Bottom right of the window)







RECOMMENDATIONS

*Remember to write double back slashes in all your paths.

*Avoid installing Python in directories with blank spaces in the name (e.g. "C:\Program Files (x86)\"), the space between words will cause failure in the script. 

*If you install Python or other files in a location with blank spaces in the name, you can escape these by adding double quotes and a backslash.



*EXAMPLE:

A path with this structure will not work: "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64"

You will need to adapt with this format "C:\\\"Program Files (x86)\"\\\"Microsoft Visual Studio\"\\Shared\\Python36_64\\python.exe"





To use these scripts read the user guide or Watch the tutorial video in YouTube omicR in R Studio (~20 min)

https://youtu.be/2dEgOBjcvM8 



For usage, please refer to the file "OmicR_User_guide.pdf" available in this repository.
