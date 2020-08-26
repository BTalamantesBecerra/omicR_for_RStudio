#READ ME FILE

#REQUIREMENTS 
#INSTALL BIOPYTHON "https://biopython.org/wiki/Download" 

#To run this script you need to provide the following handles in the command line:

#1. CALL THE PROGRAM                                                                                    Downloading_genomes.py 
#2. WRITE YOUR USER EMAIL. NCBI CAN BLOCK YOUR ACCESS IF YOU DO NOT PROVIDE THIS.                      -a your_email@mail.com
#3. ACCESSIONS NUMBERS FROM NCBI, SEPARATED BY COMMAS 
#   FOR EXAMPLE:  "NC_009328.1, NC_009329.1"                                                           -b "NC_009328.1, NC_009329.1"
#4. SELECT THE PATH WHERE YOU WANT YOUR GENOME TO BE SAVED                                             -c ~YOUR_PATH
#5. GIVE YOUR GENOME A NAME (e.g. Pogona, bacteria...etc)                                              -d GIVE_IT_A_NAME

#Notes to consider
# 1. Select the paths to your input and output files. If you are running this script in Windows, remember to add a double "\\" to your paths.
    #EXAMPLE: C:\\~PATH\Bassiana_364_M-365_F-64_F_contigs_ge_100.csv
    #Consider avoiding saving any files or programs in the "Programs File" directory as the space between "Programs" and "File" will make the script crash. 
# 2. Remember to replace ~PATH with your PATHS.
# 3. Remember to check or replace "\" by "/" if you are working in Linux.
# 4. Remember that you need to add Python to the path to be able to run this script.
#  To add python to the path you can do it by going to:
#  Control Panel > System and Security > System > Advanced System Settings > Environment Variables > System Variables > Path
#  THEN PASTE HERE THE LINK TO THE DIRECTORY WHERE YOU HAVE PYTHON INSTALLED).
#  If you do not want to add python to your path, copy the whole link to the executable file prior running any scripts. It should look like ~PATH\python.exe 
# 5. The command line to run this script should look like this:
# Downloading_genomes.py -a YOUR EMAIL -b ACCESSION_NUMBERS IN DOUBLE QUOTES AND SEPARATED BY COMMAS -c ~YOUR_PATH_WHERE_YOU_WANT_YOUR_GENOME -d GIVE_IT_A_NAME



#BACTERIA
#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe TestingPyCharm_Downloading_genomes.py -a "berenicetalamantes@yahoo.fr" -b "NC_009328.1, NC_009329.1" -c C:\\thingslap\Pipeline\GUI_Output\Upload\ -d bacteria


#Chicken
#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe Downloading_genomes.py -a "berenicetalamantes@yahoo.fr" -b "NC_006088.5, NC_006089.5, NC_006090.5, NC_006091.5, NC_006092.5, NC_006093.5, NC_006094.5, NC_006095.5, NC_006096.5, NC_006097.5, NC_006098.5, NC_006099.5, NC_006100.5, NC_006101.5, NC_006102.5, NC_006103.5, NC_006104.5, NC_006105.5, NC_006106.5, NC_006107.5, NC_006108.5, NC_006109.5, NC_006110.5, NC_006111.5, NC_006112.4, NC_006113.5, NC_006114.5, NC_006115.5, NC_028739.2, NC_028740.2, NC_006119.4, NC_008465.4, NC_006126.5, NC_006127.5" -c C:\\thingslap\Pipeline\Output_files\Genomes\ -d Chicken_vGRCg6a

#Downloading_genomes.py -a berenicetalamantes@yahoo.fr -b 'NC_009328.1', 'NC_009329.1' -c C:\\thingslap\Pipeline\Output_files\Genomes\Genome.txt

#POGONA
#Downloading_genomes.py -a berenicetalamantes@yahoo.fr -b 'GCF_900067755.1' -c C:\\thingslap\Pipeline\Output_files\Genomes\ -d Pogona

#chicken_GRCg6a = "NC_006088.5, NC_006089.5, NC_006090.5, NC_006091.5, NC_006092.5, NC_006093.5, NC_006094.5, NC_006095.5, NC_006096.5, NC_006097.5, NC_006098.5, NC_006099.5, NC_006100.5, NC_006101.5, NC_006102.5, NC_006103.5, NC_006104.5, NC_006105.5, NC_006106.5, NC_006107.5, NC_006108.5, NC_006109.5, NC_006110.5, NC_006111.5, NC_006112.4, NC_006113.5, NC_006114.5, NC_006115.5, NC_028739.2, NC_028740.2, NC_006119.4, NC_008465.4, NC_006126.5, NC_006127.5" 
#chicken_Gallus_gallus-5.0 = "NC_006088.4, NC_006089.4, NC_006090.4, NC_006091.4, NC_006092.4, NC_006093.4, NC_006094.4, NC_006095.4, NC_006096.4, NC_006097.4, NC_006098.4, NC_006099.4, NC_006100.4, NC_006101.4, NC_006102.4, NC_006103.4, NC_006104.4, NC_006105.4, NC_006106.4, NC_006107.4, NC_006108.4, NC_006109.4, NC_006110.4, NC_006111.4, NC_006112.3, NC_006113.4, NC_006114.4, NC_006115.4, NC_028739.1, NC_028740.1, NC_006119.3, NC_008465.3, NC_006126.4, NC_006127.4, NC_008466.3"
#CHICKEN Z and W "NC_006126.5, NC_006127.5"
#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe Downloading_genomes.py -a berenicetalamantes@yahoo.fr -b 'NC_006126.5, NC_006127.5' -c C:\\thingslap\Pipeline\Output_files\Genomes\ - d Chromosome_Z_W
#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe Downloading_genomes.py -a berenicetalamantes@yahoo.fr -b 'NC_006126.5' -c C:\\thingslap\Pipeline\Output_files\Genomes\ -d Chromosome_W

import sys, getopt
import os
from Bio import Entrez

def main(argv):
    
    email = ""
    genomeAccessions = ""
    OutputGenomeFile = ""
    OutputFilePath = ""
    fileName = ""


    try:
        opts, args = getopt.getopt(argv,"a:b:c:d:",["UserEmail=","GenomeAccessions=", "OutputFilePath=", "fileName="])
    except getopt.GetoptError:
      print ('Downloading_genomes.py -a <User_Email> -b <Genome_Accessions> -c <OutputFilePath> -d <fileName>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('Downloading_genomes.py -a <User_Email> -b <Genome_Accessions> -c <OutputFilePath> -d <fileName> ')
         sys.exit()
        elif opt in ("-a", "--User_Email"):
            email = arg
        elif opt in ("-b", "--Genome_Accessions"):
            genomeAccessions = arg
        elif opt in ("-c", "--OutputFilePath"):
            OutputFilePath = arg
        elif opt in ("-d", "--fileName"):
            fileName = arg

    Entrez.email    = email


    def get_sequences_from_ID_list_line_by_line(ids):
        print(ids)
        
        DirectoryPath = OutputFilePath + fileName
        if not os.path.exists(DirectoryPath):
            os.makedirs(DirectoryPath)
    
        NameOfMyFile = DirectoryPath + '/' + fileName + ".fasta"
        file = open(NameOfMyFile, 'w')
        counter = 1
        
        for seq_id in ids:
            handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
            #Read Data
            AllLines = handle.readlines()


            #PRINT AND WRITE LANE 0
            NameOfGenome_Line0 = AllLines[0].splitlines()
            print(NameOfGenome_Line0)
            
            str0 = ''.join(NameOfGenome_Line0)
            file.write(str0)
            file.write('\n')

            #Create a loop to read all rows in a file

            genome_without_header = AllLines[1:]
            listLenght = len(genome_without_header)
            #print(listLenght)
         
            complete_genome_string = ""

            for x in range(0,listLenght):
                tempList = genome_without_header[x].splitlines()
                tempString = tempList[0]
                complete_genome_string += tempString
            file.write(complete_genome_string)
            file.write('\n')

            print(counter)
            counter += 1

        file.close()

    list_of_accessions = genomeAccessions.split(',')
    get_sequences_from_ID_list_line_by_line(list_of_accessions)



if __name__ == "__main__":
    main(sys.argv[1:])
