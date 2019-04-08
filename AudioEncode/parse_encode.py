"""
Encoder context

ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3

"""

import os
import re

from os.path import isdir, join

# Path for FFMPEG file location

FFMPEG ="c:/Users/347905/Downloads/ffmpeg-4.1.1-win64-static/bin/ffmpeg.exe"

# Path to parse
PATH_TO_PARSE = "c:/Users/347905/Downloads"


# Function for conversion of wav file to mp3, file name needs to be passed with full path
def conv_mp3(i_file):
    # Split filename to extract the name 
    # to append MP3 extension for the same file name 
    # with full path of where to write the file
    out_file, in_ext = i_file.split(".")

    #Execute command line for file conversion
    os.system(FFMPEG + " -i "+ i_file+" -vn -ar 44100 -ac 2 -b:a 128k "+ out_file+".mp3")


def list_dir_contents(path):
    lst_fldr = []
    
    # List all files of the folder
    lst_fldr = os.listdir(path)
    
    # Find WAV files and initiate conversion
    for i in lst_fldr:
        
        # Exception for files where there are issues with permission on unrecognised extensions
        try:
            bifn, iext = i.split(".")
            if iext == "wav":
                conv_mp3(path+"/"+i) #Append path to file name for conversion
        except:
            pass

    

if __name__ == "__main__":
    list_dir_contents(PATH_TO_PARSE)