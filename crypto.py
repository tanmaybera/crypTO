from random import choice
import os

class file:
    def __init__(self , filepath):
        self.filePath = filePath
        
    def _extension(self):
        extsnList = self.filePath.split('.')
        if len(extsnList) > 1:
            extnsn = extsnList[-1]
            return extnsn
        else:
            return ''
        
    def _filename(self):
        fileName = self.filePath.split('.')
        if len(fileName) > 1:
            fileN = fileName[0]
            return fileN
        else:
            return ''
        
    def _reaDer(self):
        f = open(self.filePath, 'rb')
        fileCon = bytearray(f.read())
        f.close()
        return fileCon
    
    def _converter(self , ClistorString , option):
        if option == 1:
            Llist=[ord(i) for i in ClistorString]
            return Llist
        if option == 2:
            Lstring = bytearray([i^key for i in ClistorString])
            return Lstring
        if option == 3:
            Lstring = bytearray([i^pKey for i in ClistorString])
            return Lstring
    
    def _whoDid(self):
        return os.getlogin()
    
    

def selection(selection):
    if selection == 1:
        Header="------Warning! this is a restricted script--------\
        #MD5HASH : 6e1ae1e6dc265769c42231fda0bca2db\
        --------Warning! this is a restricted software--------"
        return Header
    if selection == 2:
        tailer = "------Warning! this is a restricted software--------\
        #MD5HASH : 6e1ae1e6dc265769c42231fda0bca2db\
        ------Warning! this is a restricted software--------"
        return tailer


if __name__ == '__main__':
    global key
    global pKey
    newFileC = bytearray()
    key=int(ord('T'))
    
    # Input file name
    # new file e.g -> 'password.xlsx'
    # decryption file will be e.g - > 'password.crypTo'
    # new file extension will be - ".crypTo"
    filePath = 'password.xlsx'
    #-------------------------
    
    fCon = file(filePath)
    if ''.join(chr(i) for i in fCon._converter(fCon._reaDer()[0:163], 2)) != selection(1) \
    and ''.join(chr(i) for i in fCon._converter(fCon._reaDer()[len(fCon._reaDer())-163: len(fCon._reaDer())], 2)) != selection(2):
        if len(fCon._extension()) >= 3:
            pKey = choice(range(120 , 255))
        else:
            pKey = choice(range(1 , 120))
        flist = {1 : fCon._converter(fCon._converter(selection(1), 1), 2),
                2 : fCon._converter(fCon._converter(fCon._whoDid().ljust(15), 1), 2),
                3 : fCon._converter(fCon._converter(str(pKey).ljust(3), 1), 2),
                4 : fCon._converter(fCon._converter(fCon._extension().ljust(15), 1), 3),
                5 : fCon._converter(fCon._reaDer(), 3),
                6 : fCon._converter(fCon._converter(selection(2), 1), 2)}
        for i in range(1, 7):
            newFileC.extend(flist.get(i))
        nF = open(fCon._filename()+'.crypTo', 'wb')
        nF.write(newFileC)
        nF.close()
        print ("Encryption Done. New File Name is - "+fCon._filename()+'.crypTo')
        
    if ''.join(chr(i) for i in fCon._converter(fCon._reaDer()[0:163], 2)) == selection(1) \
    and ''.join(chr(i) for i in fCon._converter(fCon._reaDer()[len(fCon._reaDer())-163: len(fCon._reaDer())], 2)) == selection(2):
        whoDid = ''.join(chr(i) for i in fCon._converter(fCon._reaDer()[163:178], 2)).strip()
        pKey = int(''.join(chr(i) for i in fCon._converter(fCon._reaDer()[178:181], 2)).strip())
        extn = ''.join(chr(i) for i in fCon._converter(fCon._reaDer()[181:196], 3)).strip()
        dcrypF = fCon._converter(fCon._reaDer()[196:len(fCon._reaDer())-163], 3)
        nF = open(fCon._filename()+'.'+extn, 'wb')
        nF.write(dcrypF)
        nF.close()
        print ("Decryption Done. Original File Name is - "+fCon._filename()+'.'+extn)
        
