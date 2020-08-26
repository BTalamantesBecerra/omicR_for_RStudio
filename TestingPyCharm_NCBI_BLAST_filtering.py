#READ ME FILE

#REQUIREMENTS 
#INSTALL BLAST+ "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/"
# if you have windows select "ncbi-blast-2.10.0+-x64-win64.tar.gz" 

#To run this script you need to provide the following handles in the command line:

#1. CALL THE PROGRAM                                                                                    
#2. SELECT THE PATH TO YOUR DATABASE                                                                    -a ~PATH and input BLAST
#4. SELECT THE OUTPUT PATH OR THE LOCATION YOU WANT YOUR BLAST                                          -b ~PATH\output_Location\
#5. CHOOSE A NAME FOR YOUR BLAST OUTPUT FILE                                                            -c Name of your output file. e.g. BLAST_OUTPUT.txt
#10. SELECT YOUR PERCENTAGE OVERLAP. DEFAULT IS 80%.IF YOU ARE UNSURE DON'T USE THIS PARAMETRE          -d 0.8
#11. SELECT YOUR BITSCORE VALUE, DEFAULT IS 50. IF YOU ARE UNSURE DON'T USE THIS PARAMETRE              -e 50



#THE COMMAND LINE USED FOR BLAST MUST HAVE THE FOLLOWING PARAMETRES FOR THIS SCRIPT TO WORK!

#blastn
#-task dc-megablast
#-db
#-query
#-out
# -word_size
#-perc_identity
#-num_threads
# -outfmt ' 6 qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen"')


import sys, getopt
import os

def main(argv):

    a_BLAST_input_path_and_file_ = "" 
    b_Output_Path_= ""
    c_Output_file_name = "_BLAST" 

    #FIlTERING PARAMETRES

    d_Percentage_overlap = 0.8
    e_bitscore = 50

    try:
        opts, args = getopt.getopt(argv,"a:b:c:d:e:",["a_BLAST_input_path_and_file_=",
                                                                "b_Output_Path_=",
                                                                "c_Output_file_name=",
                                                                "d_Percentage_overlap=",
                                                                "e_bitscore=",
                                                                ])
    except getopt.GetoptError:
        
      print ("ERROR:")   
      print ('CHECK YOUR INPUT HANDLES')
      print("NCBI_BLAST_filtering.py -a <a_BLAST_input_path_and_file_> -b <b_Output_Path_> -c <c_Output_file_name> -d <d_Percentage_overlap> -e <e_bitscore> ")
      sys.exit(2)
    for opt, arg in opts:
        if opt in ( '-h'):
             print ("HELP")   
             print ('NCBI_BLAST_filtering.py -a <a_BLAST_input_path_and_file_> -b <b_Output_Path_> -c <c_Output_file_name> -d <d_Percentage_overlap> -e <e_bitscore>')
             sys.exit()
         
        elif opt in ("-a", "--a_BLAST_input_path_and_file_"):
            a_BLAST_input_path_and_file_ = arg
            
        elif opt in ("-b", "--b_Output_Path_"):
            b_Output_Path_ = arg
            
        elif opt in ("-c", "--c_Output_file_name"):
            c_Output_file_name = arg
            
        elif opt in ("-d", "--d_Percentage_overlap"):
            d_Percentage_overlap = float(arg)
            
        elif opt in ("-e", "--e_bitscore"):
            e_bitscore = int(arg)


    print('\n')
    print("Percentage Overlap")
    print(d_Percentage_overlap)
    print('\n')
    print("Bitscore")
    print(e_bitscore)
    print('\n')
    ###################################################################################################################################


    #FILTERING BLAST OUTPUTFILE

    #BLAST FILTERING PARAMETRES

    
   
    qseqid = 0
    sacc = 1
    stitle = 2
    qseq = 3
    sseq = 4
    nident = 5
    mismatch = 6
    pident = 7
    length = 8
    evalue = 9
    bitscore = 10
    qstart = 11
    qend = 12
    sstart = 13
    send = 14
    gapopen = 15
    gaps = 16
    qlen = 17
    slen = 18
    PercentageOverlapINT = 19


    BLAST_OUTPUT_FILE = a_BLAST_input_path_and_file_

    file = open(BLAST_OUTPUT_FILE, 'r')
    filtered_file = b_Output_Path_ + c_Output_file_name + "_filtered.txt"
    filtered_files = open (filtered_file, "w+")

    #headers
    AllHeadersFromFilteredFile = ""
    AllHeadersFromFilteredFile = ( "qseqid" + '\t' + "sacc" + '\t' + "stitle" + '\t' +
                                   "qseq" + '\t' + "sseq" + '\t' + "nident" + '\t' + "mismatch"+ '\t' +
                                   "pident" + '\t' + "length" + '\t' + "evalue"+ '\t' +
                                   "bitscore" + '\t' + "qstart" + '\t' + "qend" + '\t' + "sstart" + '\t' +
                                   "send" + '\t' + "gapopen" + '\t' + "gaps" + '\t' +
                                   "qlen"+ '\t' + "slen" + '\t' + "PercentageOverlap" + '\n')
    filtered_files.write(AllHeadersFromFilteredFile)


    #Reading files

    tempstring = "temp"
    while tempstring:
        tempstring = file.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()

        x = templine[0]
        rowlist= x.split('\t')

        
        columns = (rowlist[qseqid] + '\t' + rowlist[sacc] + '\t' + rowlist[stitle]+ '\t' +
                   rowlist[qseq]+ '\t' + rowlist[sseq]+ '\t'  + rowlist[nident]+ '\t' + rowlist[mismatch]+ '\t' +
                   rowlist[pident] + '\t' + rowlist[length] + '\t' + rowlist[evalue]+ '\t' +
                   rowlist[bitscore]+ '\t' + rowlist[qstart]+ '\t' + rowlist[qend]+ '\t' + rowlist[sstart]+ '\t' +
                   rowlist[send] + '\t' + rowlist[gapopen] + '\t' + rowlist[gaps]+ '\t' +
                   rowlist[qlen]  + '\t' + rowlist[slen] + '\t')


        Querylength = int(rowlist[qlen])
        Length = int(rowlist[length])
        SubjectLength = int(rowlist[slen])

        min_length = min(Querylength, SubjectLength)
        
        PercentageOverlap = (Length / min_length)
        
        rowlist.append(str(PercentageOverlap))
        columns = (rowlist[qseqid] + '\t' + rowlist[sacc] + '\t' + rowlist[stitle]+ '\t' +
                   rowlist[qseq]+ '\t' + rowlist[sseq]+ '\t'  + rowlist[nident]+ '\t' + rowlist[mismatch]+ '\t' +
                   rowlist[pident] + '\t' + rowlist[length] + '\t' + rowlist[evalue]+ '\t' +
                   rowlist[bitscore]+ '\t' + rowlist[qstart]+ '\t' + rowlist[qend]+ '\t' + rowlist[sstart]+ '\t' +
                   rowlist[send] + '\t' + rowlist[gapopen] + '\t' + rowlist[gaps]+ '\t' +
                   rowlist[qlen]  + '\t' + rowlist[slen] + '\t' + rowlist[PercentageOverlapINT] + '\n' )




        #FILTERING STEP 1 <<<<< DEFAULT "Percentage overlap >80% or 0.8" >>>>> AND <<<<< DEFAULT "BitScore >50" >>>>>

        #HANDLES

        if float(rowlist[PercentageOverlapINT]) >= d_Percentage_overlap:
            if float(rowlist[bitscore]) >= e_bitscore:
                filtered_files.write(columns)

    file.close() 
    filtered_files.close()

    #TO BE CHECKED

    filtered_files_2 = open(filtered_file,'r')
 

    ###################################################################################################################################
    #####################################################PART 3

        #FILTERING STEP 2
    
    
    filter_part2_path_and_name = b_Output_Path_ + c_Output_file_name + "_sorted.txt"
    filtered_files_part2= open (filter_part2_path_and_name, "w")


   

    #headers
    AllHeadersFromFilteredFile = ""
    AllHeadersFromFilteredFile = ( "qseqid" + '\t' + "sacc" + '\t' + "stitle" + '\t' +
                                   "qseq" + '\t' + "sseq" + '\t' + "nident" + '\t' + "mismatch"+ '\t' +
                                   "pident" + '\t' + "length" + '\t' + "evalue"+ '\t' +
                                   "bitscore" + '\t' + "qstart" + '\t' + "qend" + '\t' + "sstart" + '\t' +
                                   "send" + '\t' + "gapopen" + '\t' + "gaps" + '\t' +
                                   "qlen"+ '\t' + "slen" + '\t' + "PercentageOverlap" + '\n')
    filtered_files_part2.write(AllHeadersFromFilteredFile)


    #Reading files


    lst_lst = []

    
    counter = 0 

    tempstring = "temp"
    while tempstring:
        tempstring = filtered_files_2.readline()
        if tempstring == "":
            break
        if counter != 0:
            templine = tempstring.splitlines()

            x = templine[0]
            rowlist_2= x.split('\t')

            lst_lst.append(rowlist_2)



            columns = (rowlist_2[qseqid] + '\t' + rowlist_2[sacc] + '\t' + rowlist_2[stitle]+ '\t' +
                       rowlist_2[qseq]+ '\t' + rowlist_2[sseq]+ '\t'  + rowlist_2[nident]+ '\t' + rowlist_2[mismatch]+ '\t' +
                       rowlist_2[pident] + '\t' + rowlist_2[length] + '\t' + rowlist_2[evalue]+ '\t' +
                       rowlist_2[bitscore]+ '\t' + rowlist_2[qstart]+ '\t' + rowlist_2[qend]+ '\t' + rowlist_2[sstart]+ '\t' +
                       rowlist_2[send] + '\t' + rowlist_2[gapopen] + '\t' + rowlist_2[gaps]+ '\t' +
                       rowlist_2[qlen]  + '\t' + rowlist_2[slen] + '\t' + rowlist_2[PercentageOverlapINT] + '\n' )



        counter += 1


        #READ THE NEW FILE AND ENTER THE LOOP

    #SORTING

    list.sort(lst_lst, key = lambda DataRow_0: float(DataRow_0[pident]), reverse=True)
    list.sort(lst_lst, key = lambda DataRow_2: float(DataRow_2[PercentageOverlapINT]), reverse=True) 
    list.sort(lst_lst, key = lambda DataRow_1: float(DataRow_1[bitscore]), reverse=True)
    list.sort(lst_lst, key = lambda DataRow_3: DataRow_3[qseqid])

    Dictionary_lst_lst = {}
    

    #Reading list_list
    length = len(lst_lst)
    for i in range(length):
        temp_rowlist = lst_lst[i]

        temp_rowlist_length = len(temp_rowlist)

            
        if temp_rowlist_length != 20:
            print("length of tem_row_list_is:")
            print(temp_rowlist_length)
            continue

        row_string_for_output = ""
        
        Variable_QSeqID = temp_rowlist[qseqid]

        try:
            for j in range(temp_rowlist_length - 1):
                temp_string = temp_rowlist[j]
                row_string_for_output += (temp_string + "\t")

            row_string_for_output += temp_rowlist[temp_rowlist_length - 1]
            row_string_for_output += "\n"

        except IndexError:
            print("Exception thrown")
        print(row_string_for_output)

        #Tuple
        TheTuple_rowlist = (Variable_QSeqID, row_string_for_output)

        if Variable_QSeqID in Dictionary_lst_lst:
            print("key already in dictionary")
        else:
            Dictionary_lst_lst [Variable_QSeqID] = row_string_for_output
            filtered_files_part2.write(row_string_for_output)

    
                
    filtered_files_part2.close()
    filtered_files_2.close() 


if __name__ == "__main__":
    main(sys.argv[1:])

