import pefile
# Open the PE file using the pefile library
def getImports(filePath):
    pe = pefile.PE(filePath)
    imports = [entry.dll.decode('utf-8') for entry in pe.DIRECTORY_ENTRY_IMPORT]
    return imports
# Input a file to identify the dependencies
filePath = 'path/to/executable.exe'
# Print the found dependencies
print(getImports(filePath))
