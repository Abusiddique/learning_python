'''
1 Read the config file, get file path 
2 Read the file if exist
3 If the file does not exist , create one
'''
from configparser import ConfigParser 

parser = ConfigParser()
parser.read('input.conf')
file_path = parser.get('INPUT_FILE', 'path')

try:
	open_file = open(file_path, "rt")
	print('File content: ' + str(open_file.read()))
	open_file.close()
	
except Exception as e:
	print("File does'nt exist creating a file")
	open_file=open(file_path,"w")
	open_file.write('Created a new file')
	open_file.close()

finally:
	print('Done with file processing')