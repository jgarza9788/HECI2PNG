# this will convert all HEIC to pngs for a specific folder

import os
import pyask
from heic2png import HEIC2PNG

def bar(num,denom,length=50,fillchar='#',emptychar=' '):
    fillnum = ((int)( (num/denom) * length))
    return '[' + ( fillnum * fillchar ).ljust(length,emptychar)  + ']' + f" {(num/denom)*100.0:.2f}%     " 


if __name__ == '__main__':

    folder = pyask.ask_folder()
    files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for index,f in enumerate(files):
        print(bar(index+1,len(files),length=100,emptychar='_'))
        # print(f)
        try:
            heic_img = HEIC2PNG(f.replace('\\\\','\\'))
            nfile = heic_img.save() 
            print(nfile)
        except Exception as e:
            print(e)
