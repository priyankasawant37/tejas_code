import os
from googletrans import Translator
translator = Translator()

#import configparser
#config = configparser.ConfigParser()
#config.read('ConfigFile.properties')
source_dir =  'ToPriya_RawData/'
dest_dir = 'OutputPriya_RawData/'
with os.scandir(source_dir) as dir_contents:
    for i in dir_contents:
        with open(source_dir+i.name,  'r') as read_file:
            write_file = open(dest_dir+i.name,  'a')
            for line in read_file:
                try:
                    key =  line.split('=')[0]
                    value = line.split('=')[1]
                    print(translator.translate(value, dest='es').text)
                    write_file.write(key+'='+translator.translate(value, dest='es').text+'\n')
                except Exception as e:
                    print("Error: ", e)
            write_file.close()


