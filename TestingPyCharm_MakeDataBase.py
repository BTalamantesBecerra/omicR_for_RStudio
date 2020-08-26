#READ ME FILE

#REQUIREMENTS 
#INSTALL BLAST+ "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/"
# if you have windows select "ncbi-blast-2.10.0+-x64-win64.tar.gz" 

#To run this script you need to provide the following handles in the command line:

#1. CALL THE PROGRAM                                                                                    MakeDataBase.py
#2. SELECT THE PATH TO THE "Bin" directory of NCBI +                                                    -a ~PATH\blast-2.8.0+\bin
#3. SELECT THE PATH TO THE LOCATION OF YOUR FASTA FILE TO BE BLASTED                                    -b ~PATH\yourfastafile.fasta
#4. SELECT THE DATABASE TYPE. IF IT IS NUCLEOTIDES TYPE "nucl" if it is proteins type "prot"            -c nucl

#Notes to consider
# 1. Select the paths to your input and output files. If you are running this script in Windows, remember to add a double "\\" to your paths.
    #EXAMPLE: C:\\~PATH\Bassiana_364_M-365_F-64_F_contigs_ge_100.csv
    #Consider avoiding saving any files or programs in the "Programs File" directory as the space between "Programs" and "File" will make the script crash. 
# 2. Remember to replace ~PATH with your PATHS.
# 3. Remember that you need to add BLAST+ and Python to the path to be able to run this script.
#       Adding python to the path
        #You can do it by going to:
#        Control Panel > System and Security > System > Advanced System Settings > Environment Variables > System Variables > Path (Click on EDIT)
#       THEN PASTE THE LINK TO THE DIRECTORY WHERE YOU HAVE PYTHON INSTALLED).
#       If you do not want to add python to your path, copy the whole link to the executable file prior running any scripts.
#       It should look like ~PATH\blastn.exe or ~PATH\python.exe 
## 4. The command line to run this script should look like this:
# MakeDataBase.py -a ~PATH\blast-2.8.0+\bin -b ~PATH\yourfastafile.fasta -c nucl


# HERE!! C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe TestingPyCharm_MakeDataBase.py -a C:\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\thingslap\Pipeline\GUI_Output\Upload\bacteria\bacteria.fasta -c nucl

# C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Chicken_vGRCg6a\Chicken_vGRCg6a.fasta -c nucl

#POGONA C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\pogona\genome_assemblies_genome_fasta\ncbi-genomes-2020-05-10\GCF_900067755.1_pvi1.1_genomic.fna\GCF_900067755.1_pvi1.1_genomic.fna -c nucl
#Chrysemis_picta  C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Chrysemis_picta_ZW\genome_assemblies_genome_fasta\ncbi-genomes-2020-05-11\GCA_000241765.3_Chrysemys_picta_BioNano-3.0.4_genomic.fna\GCA_000241765.3_Chrysemys_picta_BioNano-3.0.4_genomic.fna -c nucl
#Python_Molurus C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Python_molurus\GCA_000186305.2_Python_molurus_bivittatus-5.0.2_genomic.fna\GCA_000186305.2_Python_molurus_bivittatus-5.0.2_genomic.fna -c nucl
#King cobra C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\king_cobra\GCA_000516915.1_OphHan1.0_genomic.fna\GCA_000516915.1_OphHan1.0_genomic.fna -c nucl
#Crocodile C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\crocodile\GCF_001723895.1_CroPor_comp1_genomic.fna\GCF_001723895.1_CroPor_comp1_genomic.fna -c nucl
#Anolis_caroliensis C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Anolis_caroliensis\GCA_000090745.2_AnoCar2.0_genomic.fna\GCA_000090745.2_AnoCar2.0_genomic.fna -c nucl
#Gavialis  C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Gavialis\GCF_001723915.1_GavGan_comp1_genomic.fna\GCF_001723915.1_GavGan_comp1_genomic.fna -c nucl
#Pelodiscus C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Pelodiscus\GCA_000230535.1_PelSin_1.0_genomic.fna\GCA_000230535.1_PelSin_1.0_genomic.fna -c nucl
#Chelonia_mydas C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Chelonia_mydas\GCF_000344595.1_CheMyd_1.0_genomic.fna\GCF_000344595.1_CheMyd_1.0_genomic.fna -c nucl

#Alligator
#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Alligator\GCA_000281125.4_ASM28112v4_genomic.fna\GCA_000281125.4_ASM28112v4_genomic.fna -c nucl
#ChromosomeW
#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Output_files\Genomes\Gallus_gallus_chromosome_W\chromosome_w.fasta -c nucl
#SCAFOLD POGONA
#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Pogona_Genome\bdup1.Jul2013.fasta -c nucl
#CONTIGS POGONA C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe MakeDataBase.py -a C:\\thingslap\casual_work_2020\blast-2.8.0+\bin\ -b C:\\thingslap\Pipeline\Pogona_Genome\bdup1.Jul2013.contigs.fasta -c nucl


import sys, getopt
import os

def main(argv):
    
    Path_To_NCBI_BLAST_Bin_Directory = ""
    Path_To_Database_Fasta_File = ""
    Data_Base_Type = "nucl"




    try:
        opts, args = getopt.getopt(argv,"a:b:c:",["Path_To_NCBI_BLAST_Bin_Directory=","Path_To_Database_Fasta_File=", "Data_Base_Type="])
    except getopt.GetoptError:
      print ('MakeDataBase.py -a <Path_To_NCBI_BLAST_Bin_Directory> -b <Path_To_Database_Fasta_File> -c <Data_Base_Type (e.g. write "nucl" for nucleotides or "prot" for proteins)>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('MakeDataBase.py -a <Path_To_NCBI_BLAST_Bin_Directory> -b <Path_To_Database_Fasta_File> -c <Data_Base_Type (e.g. write "nucl" for nucleotides or "prot" for proteins)> ')
         sys.exit()
        elif opt in ("-a", "--Path_To_NCBI_BLAST_Bin_Directory"):
            Path_To_NCBI_BLAST_Bin_Directory = arg
        elif opt in ("-b", "--Path_To_Database_Fasta_File"):
            Path_To_Database_Fasta_File = arg
        elif opt in ("-c", "--Data_Base_Type"):
            Data_Base_Type = arg




    #CREATE DATABASE FOR RUNNING BLAST IN WINDOWS
    CreateDataBase = Path_To_NCBI_BLAST_Bin_Directory + "makeblastdb -in " + Path_To_Database_Fasta_File + " -dbtype " + Data_Base_Type
    print(CreateDataBase)
    os.system(CreateDataBase)

if __name__ == "__main__":
    main(sys.argv[1:])


