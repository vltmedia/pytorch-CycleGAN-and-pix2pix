
import shutil
import glob
from random import randrange

from options.util_options import UtilOptions


class CopyFilesToDirectory:
   
    def __init__(self):
        print("init 1")
        self.opt = UtilOptions().parse()
        print("init 2")
        
        self.inputDirectory = self.opt.dataroot
        self.outputDirectory = self.opt.output
        self.extension = self.opt.extension
        self.shoutCount = self.opt.shot_count
        self.files = glob.glob(self.opt.dataroot+'/*.'+self.opt.extension)
        self.copied = []
        print(self.opt)
        
        
   

    def ProcessFiless(self):
        for ran in range(0, self.shoutCount):
            randomm = randrange(len(self.files) - 1)
            if randomm not in self.copied:
                self.copied.append(randomm)
                print("Copying | ",self.files[randomm])
                shutil.copy(self.files[randomm], self.outputDirectory)

if __name__ == '__main__':
    cop = CopyFilesToDirectory()
    cop.ProcessFiless()