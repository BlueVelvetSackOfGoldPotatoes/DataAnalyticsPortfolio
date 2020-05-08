import sys
import pandas as pd
# @fileName is the name of the file where content will be saved to.
# @content is the data that will be saved to fileName.

class saveHandler :
    def __init__(self, argsList):
        
        # List of arguments: 0) file name 1) content of file 2) type of file to be saved to.
        # argsList = [fileName, fileContent, fileExtension]
        argsList = checkArgs(argsList)
        self.name = argsList['fileName']
        self.content = argsList['fileContent']
        self.extension = argsList['fileExtension']

# Check and correct incoming arguments.
def checkArgs (argsList) :
    if argsList['fileContent'] is None:
        print("Empty file! Creating file...")
        argsList['fileContent'] = ''

    if argsList['fileName'] is None:
        print("No name provided for saved file! Creating file named \'savedFile.txt\'...")
        argsList['fileName'] = 'savedFile.txt'

    if argsList['fileExtension'] is None:
        saveObject.extension = 'txt'

    return argsList

def save(self) :
    if self.extension is 'txt':
        with open(self.name, mode='w') as file_object:
            print(self.content, file=file_object)
    elif self.extension is 'json':
        df = pd.DataFrame(data=self.content).T
        df.to_json(self.name)