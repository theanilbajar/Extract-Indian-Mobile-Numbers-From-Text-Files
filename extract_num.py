import sys, os, re
import glob        #Extract file names from a directory  
import errno 

path = sys.argv[1]+"*.txt"   #Path of all the text files .in the given directory
file_path = glob.glob(path) #Find list of all the demo text files

#Regular Expression to extract all type of Indian mobile numbers.
reg_ex = "(?:(?:\+|0{0,2})91(\s*[\\-]\s*)?|[0]?)?[789]\d{2}\s*\d{3}\s*\d{4}"    

for filename in file_path:
    try:
        with open(filename) as f: 		#Open the file filename as a file
            lines = f.read()      		#Read lines of the file
            matches = re.finditer(reg_ex, lines)#Capture all the matches in the lines or the file f.
            for match in matches:              	#Traverse through matches tuple and printing all the matched mobile numbers 
                print ("{match}".format(match = match.group())) 
	    f.close()
    except IOError as err:
        if err.errno != errno.EISDIR:
            print("File " + filename +" doesn't exist")
    except AttributeError as aerr:
	raise 
