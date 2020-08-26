#C:\Users\s433088\AppData\Local\Programs\Python\Python36-32\python.exe TestingPyCharm_Mkfasta.py -a C:\\thingslap\Pipeline\Input_files\Bassiana_364_M-365_F-64_F_contigs_ge_100_for_testing.csv -b C:\\thingslap\Pipeline\GUI_Output\Upload\ -c Bassiana_364_M-365_F-64_F_contigs_ge_100_for_testing -d 7 -e 8 -f 2

import sys, getopt

def main(argv):
    
    a_InputCSVFileName = ""
    b_OutputPATH = ""
    c_OutputFileName = ""
    d_Row_Where_header_starts = 0
    e_rowWhereDataStarts = 0
    f_SEQUENCE_COLUMN = 0
    #g_AVG_READS = 0
    #i_Nbases = 0

    OutputRows = ""
    index = 1
    index_2 = 1
    c_OutputFileName = "your_original_file"
    

    try:
        opts, args = getopt.getopt(argv,"a:b:c:d:e:f:",["a_InputCSVFileName=","b_OutputPATH=","c_OutputFileName=","d_Row_Where_header_starts=","e_rowWhereDataStarts=","f_SEQUENCE_COLUMN="])
                                   
 
    except getopt.GetoptError:
      print("ERROR: Check your input values")
      print ('Mkfasta_final.py -a <a_InputCSVFileName> -b <b_OutputPATH> -c <Give it a name like "YOUR_FILE"> -d <d_Row_Where_header_starts. NOTE: Start_counting_from_zero> -e <row_Where_Data_Starts_NOTE: Start_counting_from_zero> -f <Sequence_Column_Number_NOTE: Start_counting_from_zero>')
             
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('Mkfasta_final.py -a <a_InputCSVFileName> -b <b_OutputPATH> -c <Give it a name like "YOUR_FILE"> -d <d_Row_Where_header_starts. NOTE: Start_counting_from_zero> -e <row_Where_Data_Starts_NOTE: Start_counting_from_zero> -f <Sequence_Column_Number_NOTE: Start_counting_from_zero>')
         sys.exit()
        elif opt in ("-a", "--a_InputCSVFileName"):
            a_InputCSVFileName = arg
        elif opt in ("-b", "--b_OutputPATH"):
            b_OutputPATH = arg
        elif opt in ("-c", "--c_OutputFileName"):
            c_OutputFileName = arg
        elif opt in ("-d", "--d_Row_Where_header_starts"):
            d_Row_Where_header_starts = int(arg)
        elif opt in ("-e", "--e_rowWhereDataStarts"):
            e_rowWhereDataStarts = int(arg)
        elif opt in ("-f", "--f_SEQUENCE_COLUMN"):
            f_SEQUENCE_COLUMN = int(arg)
        #elif opt in ("-g", "--g_AVG_READS"):
            #g_AVG_READS = int(arg)
        #elif opt in ("-i", "--i_Nbases"):
            #i_Nbases = int(arg)
   
        # make variables


    Output_path_and_name = b_OutputPATH + c_OutputFileName + ".fasta"
    Output_extra_file = b_OutputPATH + c_OutputFileName + "_InputFile_with_unique_ID.txt"
    inputFile = open(a_InputCSVFileName, errors='ignore')
    OutputFile = open(Output_path_and_name, 'w')
    Output_EXTRA = open(Output_extra_file, 'w')

    # MAKING FASTA FILE

    # Read through and skip header row

    for c in range(0, d_Row_Where_header_starts):
        HeaderTemp = inputFile.readline()

    # Reading through the rows and breaking at the end of the data

    tempstring = "temp"
    while tempstring:
        tempstring = inputFile.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split(",")
        #SeqID = rowlist[g_AVG_READS]
        TrimmedSequence = rowlist[f_SEQUENCE_COLUMN]
        #NBases = rowlist[i_Nbases]

        OutputRows = ">" + str(index) + '\n' + TrimmedSequence + '\n'
        #OutputRows = ">" + str(index) + "_" + SeqID + "_" + NBases + '\n' + TrimmedSequence + '\n'
        index += 1
        OutputFile.write(OutputRows)

    inputFile.close()
    OutputFile.close()

    # MAKING INPUT FILE FOR FILTERING AFTER BLAST

    # READ AND WRITE AGAIN THE INPUT FILE FOR THIS SCRIPT
    # Original File
    # Reading and writing headers

    inputFile_2 = open(a_InputCSVFileName, errors='ignore')
    AllHeadersJoined_inputFile_2 = ""

    for c in range(0, d_Row_Where_header_starts):
        headerTemp = inputFile_2.readline()
        
    headerLine = headerTemp.splitlines()
    y = headerLine[0]
    headerList = y.split(",")
    header_tab_delimited = ""
    for j in range (0, (len(headerList)-1)):
        header_tab_delimited += headerList[j] + '\t'
    header_tab_delimited += headerList[(len(headerList)-1)]
    AllHeadersJoined_inputFile_2 += ( "FastaFileID" + '\t' +  header_tab_delimited + '\n') #headerList[f_SEQUENCE_COLUMN]
    Output_EXTRA.write(AllHeadersJoined_inputFile_2)

    # Original File
    # Reading through the rows and breaking at the end of the data. Writing it into a
    # new document and adding an extra column as Fasta File ID.

    tempstring = "temp"
    while tempstring:
        tempstring = inputFile_2.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split(",")
        data_tab_delimited = ""
        for i in range(0, (len(rowlist)-1)):
            data_tab_delimited += rowlist[i] + '\t'
        data_tab_delimited += rowlist[(len(rowlist)-1)]
        #SequenceID = rowlist[f_SEQUENCE_COLUMN]
        FastaFileID = (str(index_2))
        index_2 += 1
        data = ( FastaFileID + '\t' + data_tab_delimited + '\n') 
        Output_EXTRA.write(data)

    inputFile_2.close()
    Output_EXTRA.close()


if __name__ == "__main__":
    main(sys.argv[1:])








    
