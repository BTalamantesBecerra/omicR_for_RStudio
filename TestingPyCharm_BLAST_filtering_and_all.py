#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe TestingPyCharm_BLAST_filtering_and_all.py
#-x C:\\thingslap\ncbi-blast-2.6.0+-x64-win64.tar\ncbi-blast-2.6.0+-x64-win64\ncbi-blast-2.6.0+\bin\
#-y dc-megablast
#-a C:\\thingslap\Pipeline\Output_files\Genomes\Chicken_vGRCg6a\Chicken_vGRCg6a.fasta
#-b C:\\thingslap\Pipeline\Output_files\Bassiana_364_M-365_F-64_F_contigs_ge_100.fasta
#-c C:\\thingslap\Pipeline\GUI_Output\Upload\
#-d Test2_Bassiana_Vs_chicken_PYTHON_2
#-e 11 -f 70 -g 4 -i 6 -j 0.01 -k 30
#-l C:\\thingslap\Pipeline\Output_files\Bassiana_364_M-365_F-64_F_contigs_ge_100_InputFile_with_unique_ID.txt

#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe TestingPyCharm_BLAST_filtering_and_all.py -x C:\\thingslap\ncbi-blast-2.6.0+-x64-win64.tar\ncbi-blast-2.6.0+-x64-win64\ncbi-blast-2.6.0+\bin\ -y FALSE -a C:\\thingslap\Pipeline\Output_files\Genomes\Chicken_vGRCg6a\Chicken_vGRCg6a.fasta -b C:\thingslap\Pipeline\GUI_Output\Upload\Bassiana_364_M-365_F-64_F_contigs_ge_100_for_testing.fasta -c C:\\thingslap\Pipeline\GUI_Output\Upload\ -d Test3_Bassiana_Vs_chicken_FALSE -e 11 -f 70 -g 4 -i 6 -j 0.01 -k 30 -l C:\\thingslap\Pipeline\GUI_Output\Upload\Bassiana_364_M-365_F-64_F_contigs_ge_100_for_testing_InputFile_with_unique_ID.txt


#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe BLAST_filtering_and_all.py
#-a C:\\thingslap\Pipeline\Output_files\Genomes\Chicken_vGRCg6a\Chicken_vGRCg6a.fasta
#-b C:\\thingslap\Pipeline\Output_files\Bassiana_364_M-365_F-64_F_contigs_ge_100.fasta
#-c C:\\thingslap\Pipeline\GUI_Output\Upload\
#-d Test_Bassiana_Vs_chicken_PYTHON
#-e 11 -f 70 -g 4 -i 6 -j 0.01 -k 30
#-l C:\\thingslap\Pipeline\Output_files\Bassiana_364_M-365_F-64_F_contigs_ge_100_InputFile_with_unique_ID.txt

import sys, getopt
import os

def main(argv):
    
    x_Path_to_NCBI_Directory_BF = ""
    y_DC_MegaBlast_BF = ""  
    a_Data_Base_fasta = ""
    print(" the value of a_Data_Base_fasta is: " + a_Data_Base_fasta)
    b_Query_fasta_file = "" 
    c_Output_Path_= ""


    #BLAST PARAMETRES
    d_Output_file_name = "_BLAST" 
    e_word_size = "" #"20"
    f_Percentage_identity = ""#"70" 
    g_number_of_threads = "" # "4" 
    i_OutputFormat = "" # "6"
    

    #FIlTERING PARAMETRES

    j_Percentage_overlap = 0.8
    k_bitscore = 50
    l_InputFile_with_unique_ID = ""
    

    try:
        opts, args = getopt.getopt(argv,"x:y:a:b:c:d:e:f:g:i:j:k:l:",["x_Path_to_NCBI_Directory_BF=",
                                                                      "y_DC_MegaBlast_BF=",
                                                                      "a_Data_Base_fasta=",
                                                                "b_Query_fasta_file=",
                                                                "c_Output_Path_=",
                                                                "d_Output_file_name=",
                                                                "e_word_size=",
                                                                "f_Percentage_identity=",
                                                                "g_number_of_threads=",
                                                                "i_OutputFormat=",
                                                                "j_Percentage_overlap=",
                                                                "k_bitscore=",
                                                                "l_InputFile_with_unique_ID="])
    except getopt.GetoptError:
        
      print ("ERROR:")   
      print ('CHECK YOUR INPUT HANDLES')
      print('BLAST_filtering_and_all.py -a <a_Data_Base_fasta> -b <b_Query_fasta_file> -c <c_Output_Path_> -d <d_Output_file_name> -e <e_word_size> -f <f_Percentage_identity> -g <g_number_of_threads>  -i <i_OutputFormat> -j <j_Percentage_Overlap> -k <k_bitscore> -l <l_InputFile_with_unique_ID>')
      sys.exit(2)
    for opt, arg in opts:
        if opt in ( '-h'):
             print ("HELP")   
             print ('BLAST_filtering_and_all.py -a <a_Data_Base_fasta> -b <b_Query_fasta_file> -c <c_Output_Path_> -d <d_Output_file_name> -e <e_word_size> -f <f_Percentage_identity> -g <g_number_of_threads> -i <i_OutputFormat> -j <j_Percentage_Overlap> -k <k_bitscore> -l <l_InputFile_with_unique_ID>')
             sys.exit()


        elif opt in ("-x", "--x_Path_to_NCBI_Directory_BF"):
            x_Path_to_NCBI_Directory_BF  = arg
            
        elif opt in ("-y", "--y_DC_MegaBlast_BF"):
            #y_DC_MegaBlast_BF = ("-task " + arg)
            if arg == "TRUE":
                y_DC_MegaBlast_BF = "-task dc-megablast"
                

            
        elif opt in ("-a", "--a_Data_Base_fasta"):
            a_Data_Base_fasta = arg
            
        elif opt in ("-b", "--b_Query_fasta_file"):
            b_Query_fasta_file = arg
            
        elif opt in ("-c", "--c_Output_Path_"):
            c_Output_Path_ = arg
            
        elif opt in ("-d", "--d_Output_file_name"):
            d_Output_file_name = arg
            
        elif opt in ("-e", "--e_word_size"):
            e_word_size = arg
            
        elif opt in ("-f", "--f_Percentage_identity"):
            f_Percentage_identity = arg
            
        elif opt in ("-g", "--g_number_of_threads"):
            g_number_of_threads = arg
            
        elif opt in ("-i", "--i_OutputFormat"):
            i_OutputFormat = arg
            
        elif opt in ("-j", "--j_Percentage_overlap"):
            j_Percentage_overlap = float(arg)
            
        elif opt in ("-k", "--k_bitscore"):
            k_bitscore = int(arg)
            
        elif opt in ("-l", "--l_InputFile_with_unique_ID"):
            l_InputFile_with_unique_ID = arg

    print('\n')
    print("Percentage Overlap")
    print(j_Percentage_overlap)
    print('\n')
    print("Bitscore")
    print(k_bitscore)
    print('\n') 
            
        
    CommandLine_BF = (x_Path_to_NCBI_Directory_BF + "blastn " + y_DC_MegaBlast_BF 
                   + " -db " + a_Data_Base_fasta + " -query "
                   + b_Query_fasta_file + " -out " + c_Output_Path_ + d_Output_file_name + "BLAST.txt"
                    + " -word_size " + e_word_size + " -perc_identity " + f_Percentage_identity
                     + " -num_threads " + g_number_of_threads + " -outfmt " + '"' + i_OutputFormat +
                    ' qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen"')

    print(CommandLine_BF)
    os.system(CommandLine_BF)

    ###################################################################################################################################
    #####################################################PART 2

    # FILTERING BLAST OUTPUTFILE

    # BLAST FILTERING PARAMETRES

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

    BLAST_OUTPUT_FILE_BF = c_Output_Path_ + d_Output_file_name + "BLAST.txt"

    file_BF = open(BLAST_OUTPUT_FILE_BF, 'r')
    filtered_file_BF = c_Output_Path_ + d_Output_file_name + "_filtered.txt"
    filtered_files_BF = open(filtered_file_BF, "w+")

    # headers
    AllHeadersFromFilteredFile_BF = ""
    AllHeadersFromFilteredFile_BF = ("qseqid" + '\t' + "sacc" + '\t' + "stitle" + '\t' +
                                  "qseq" + '\t' + "sseq" + '\t' + "nident" + '\t' + "mismatch" + '\t' +
                                  "pident" + '\t' + "length" + '\t' + "evalue" + '\t' +
                                  "bitscore" + '\t' + "qstart" + '\t' + "qend" + '\t' + "sstart" + '\t' +
                                  "send" + '\t' + "gapopen" + '\t' + "gaps" + '\t' +
                                  "qlen" + '\t' + "slen" + '\t' + "PercentageOverlap" + '\n')
    filtered_files_BF.write(AllHeadersFromFilteredFile_BF)

    # Reading files

    tempstring = "temp"
    while tempstring:
        tempstring = file_BF.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()

        x = templine[0]
        rowlist = x.split('\t')

        columns = (rowlist[qseqid] + '\t' + rowlist[sacc] + '\t' + rowlist[stitle] + '\t' +
                   rowlist[qseq] + '\t' + rowlist[sseq] + '\t' + rowlist[nident] + '\t' + rowlist[mismatch] + '\t' +
                   rowlist[pident] + '\t' + rowlist[length] + '\t' + rowlist[evalue] + '\t' +
                   rowlist[bitscore] + '\t' + rowlist[qstart] + '\t' + rowlist[qend] + '\t' + rowlist[
                       sstart] + '\t' +
                   rowlist[send] + '\t' + rowlist[gapopen] + '\t' + rowlist[gaps] + '\t' +
                   rowlist[qlen] + '\t' + rowlist[slen] + '\t')

        Querylength_BF = int(rowlist[qlen])
        Length_BF = int(rowlist[length])
        SubjectLength_BF = int(rowlist[slen])

        min_length_BF = min(Querylength_BF, SubjectLength_BF)

        PercentageOverlap = (Length_BF / min_length_BF)

        rowlist.append(str(PercentageOverlap))
        columns = (rowlist[qseqid] + '\t' + rowlist[sacc] + '\t' + rowlist[stitle] + '\t' +
                   rowlist[qseq] + '\t' + rowlist[sseq] + '\t' + rowlist[nident] + '\t' + rowlist[mismatch] + '\t' +
                   rowlist[pident] + '\t' + rowlist[length] + '\t' + rowlist[evalue] + '\t' +
                   rowlist[bitscore] + '\t' + rowlist[qstart] + '\t' + rowlist[qend] + '\t' + rowlist[
                       sstart] + '\t' +
                   rowlist[send] + '\t' + rowlist[gapopen] + '\t' + rowlist[gaps] + '\t' +
                   rowlist[qlen] + '\t' + rowlist[slen] + '\t' + rowlist[PercentageOverlapINT] + '\n')

        # FILTERING STEP 1 <<<<< DEFAULT "Percentage overlap >80% or 0.8" >>>>> AND <<<<< DEFAULT "BitScore >50" >>>>>

        # HANDLES

        if float(rowlist[PercentageOverlapINT]) >= float(j_Percentage_overlap):
            if float(rowlist[bitscore]) >= int(k_bitscore):
                filtered_files_BF.write(columns)

    file_BF.close()
    filtered_files_BF.close()

    # TO BE CHECKED

    filtered_files_2_BF = open(filtered_file_BF, 'r')

    ###################################################################################################################################
    #####################################################PART 3

    # FILTERING STEP 2

    filter_part2_path_and_name_BF = c_Output_Path_ + d_Output_file_name + "_sorted.txt"
    # print(filter_part2_path_and_name)
    filtered_files_part2_BF = open(filter_part2_path_and_name_BF, "w")

    # headers
    AllHeadersFromFilteredFile = ""
    AllHeadersFromFilteredFile_BF = ("qseqid" + '\t' + "sacc" + '\t' + "stitle" + '\t' +
                                  "qseq" + '\t' + "sseq" + '\t' + "nident" + '\t' + "mismatch" + '\t' +
                                  "pident" + '\t' + "length" + '\t' + "evalue" + '\t' +
                                  "bitscore" + '\t' + "qstart" + '\t' + "qend" + '\t' + "sstart" + '\t' +
                                  "send" + '\t' + "gapopen" + '\t' + "gaps" + '\t' +
                                  "qlen" + '\t' + "slen" + '\t' + "PercentageOverlap" + '\n')
    filtered_files_part2_BF.write(AllHeadersFromFilteredFile_BF)

    # Reading files

    lst_lst = []

    counter = 0

    tempstring = "temp"
    while tempstring:
        tempstring = filtered_files_2_BF.readline()
        if tempstring == "":
            break
        if counter != 0:
            templine = tempstring.splitlines()

            x = templine[0]
            rowlist_2 = x.split('\t')

            lst_lst.append(rowlist_2)

            columns = (rowlist_2[qseqid] + '\t' + rowlist_2[sacc] + '\t' + rowlist_2[stitle] + '\t' +
                       rowlist_2[qseq] + '\t' + rowlist_2[sseq] + '\t' + rowlist_2[nident] + '\t' + rowlist_2[
                           mismatch] + '\t' +
                       rowlist_2[pident] + '\t' + rowlist_2[length] + '\t' + rowlist_2[evalue] + '\t' +
                       rowlist_2[bitscore] + '\t' + rowlist_2[qstart] + '\t' + rowlist_2[qend] + '\t' + rowlist_2[
                           sstart] + '\t' +
                       rowlist_2[send] + '\t' + rowlist_2[gapopen] + '\t' + rowlist_2[gaps] + '\t' +
                       rowlist_2[qlen] + '\t' + rowlist_2[slen] + '\t' + rowlist_2[PercentageOverlapINT] + '\n')

        counter += 1

        # READ THE NEW FILE AND ENTER THE LOOP

    # SORTING

    list.sort(lst_lst, key=lambda DataRow_0: float(DataRow_0[pident]), reverse=True)
    list.sort(lst_lst, key=lambda DataRow_2: float(DataRow_2[PercentageOverlapINT]), reverse=True)
    list.sort(lst_lst, key=lambda DataRow_1: float(DataRow_1[bitscore]), reverse=True)
    list.sort(lst_lst, key=lambda DataRow_3: DataRow_3[qseqid])

    Dictionary_lst_lst = {}

    # Reading list_list
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

        # Tuple
        TheTuple_rowlist = (Variable_QSeqID, row_string_for_output)

        if Variable_QSeqID in Dictionary_lst_lst:
            print("key already in dictionary")
        else:
            Dictionary_lst_lst[Variable_QSeqID] = row_string_for_output
            filtered_files_part2_BF.write(row_string_for_output)

    filtered_files_part2_BF.close()
    filtered_files_2_BF.close()

    ###################################################################################################################################
    #####################################################PART 4

    ###Writting_BLAST_results_back_into_original_file

    Output_extra_file_BF = l_InputFile_with_unique_ID
    Output_file_only_sequences_with_hits_BF = c_Output_Path_ + d_Output_file_name + "_only_sequences_with_hits.txt"
    Output_final_BLAST_File_BF = c_Output_Path_ + d_Output_file_name + "_all_sequences_with_and_without_hits.txt"
    OutputFile_BF = open(Output_final_BLAST_File_BF, 'w')
    inputFilteredBLAST_File_BF = open(filter_part2_path_and_name_BF, 'r')

    # INDEX

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

    # Reading files LISTS

    lst_lst = []

    counter = 0
    header_temp = ""
    Complete_output = ""

    tempstring = "temp"
    while tempstring:
        tempstring = inputFilteredBLAST_File_BF.readline()
        if counter == 0:
            Split_list = tempstring.splitlines()
            header_temp = Split_list[0]

        if tempstring == "":
            break
        if counter != 0:
            templine = tempstring.splitlines()

            x = templine[0]

            rowlist_2 = x.split('\t')

            lst_lst.append(rowlist_2)

            columns = (rowlist_2[qseqid] + '\t' + rowlist_2[sacc] + '\t' + rowlist_2[stitle] + '\t' +
                       rowlist_2[qseq] + '\t' + rowlist_2[sseq] + '\t' + rowlist_2[nident] + '\t' + rowlist_2[
                           mismatch] + '\t' +
                       rowlist_2[pident] + '\t' + rowlist_2[length] + '\t' + rowlist_2[evalue] + '\t' +
                       rowlist_2[bitscore] + '\t' + rowlist_2[qstart] + '\t' + rowlist_2[qend] + '\t' + rowlist_2[
                           sstart] + '\t' +
                       rowlist_2[send] + '\t' + rowlist_2[gapopen] + '\t' + rowlist_2[gaps] + '\t' +
                       rowlist_2[qlen] + '\t' + rowlist_2[slen] + '\t' + rowlist_2[PercentageOverlapINT] + '\n')

        counter += 1

    Dictionary_lst_lst = {}

    # Reading list_list

    length = len(lst_lst)
    for i in range(length):
        temp_rowlist = lst_lst[i]

        temp_rowlist_length = len(temp_rowlist)
        if temp_rowlist_length != 20:
            continue

        row_string_for_output = ""

        Variable_QSeqID = temp_rowlist[qseqid]

        try:
            for j in range(temp_rowlist_length):
                temp_string = temp_rowlist[j]
                row_string_for_output += (temp_string + "\t")
            row_string_for_output += "\n"
        except IndexError:

            print("Exception thrown")

        # Tuple
        TheTuple_rowlist = (Variable_QSeqID, row_string_for_output)

        if Variable_QSeqID in Dictionary_lst_lst:
            print("key already in dictionary")
        else:
            Dictionary_lst_lst[Variable_QSeqID] = row_string_for_output
            print(row_string_for_output)

    # OPEN THE ORIGINAL MODIFIED FILE

    Original_Modified_file_BF = open(Output_extra_file_BF, 'r')
    Only_sequences_with_hits_file_BF = open(Output_file_only_sequences_with_hits_BF, 'w')

    counter2 = 0
    Header_Temp_2 = ""

    tempstring = "temp"
    while tempstring:
        tempstring = Original_Modified_file_BF.readline()

        if counter2 == 0:
            Split_list_2 = tempstring.splitlines()
            Header_Temp_2 = Split_list_2[0]
            OutputFile_BF.write(Header_Temp_2 + "\t" + header_temp + "\n")
            Only_sequences_with_hits_file_BF.write(Header_Temp_2 + "\t" + header_temp + "\n")

        if tempstring == "":
            break

        if counter2 != 0:
            templine = tempstring.splitlines()
            x = templine[0]

            rowlist = x.split('\t')
            Temp_QSeqID = rowlist[0]

            if Temp_QSeqID in Dictionary_lst_lst:
                Corresponding_row = Dictionary_lst_lst.get(Temp_QSeqID)

                OutputFile_BF.write(x + "\t")
                OutputFile_BF.write(Corresponding_row)
                Only_sequences_with_hits_file_BF.write(x + "\t")
                Only_sequences_with_hits_file_BF.write(Corresponding_row)

            else:
                OutputFile_BF.write(
                    x + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\n")
                # print("not found in dictionary")

        counter2 += 1

    OutputFile_BF.write(Complete_output)

    Original_Modified_file_BF.close()
    OutputFile_BF.close()
    inputFilteredBLAST_File_BF.close()
    Only_sequences_with_hits_file_BF.close()
    Only_sequences_with_hits_file_BF.close()


if __name__ == "__main__":
    main(sys.argv[1:])

