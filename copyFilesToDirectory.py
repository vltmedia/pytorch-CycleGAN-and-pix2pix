# python copyFilesToDirectory.py --dataroot C:\Temp2\crops --output C:\Tempout --extension png --shot_count 24 --random_shot
# python copyFilesToDirectory.py --dataroot "M:/Projects/GAN/VG2City/01-Working/28-JJ/00-Source/01-VIDZ/GTAViceCity/DrivingVids/GTAVC-Driving1" --output "M:/Projects/GAN/VG2City/01-Working/28-JJ/00-Source/01-VIDZ/GTAViceCity/DrivingVids/temp" --extension png --shot_count 24  --random_shot


import shutil
import glob
import os
from random import randrange
import random
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
        self.currentindex = 0
        print(self.opt)
        
    def RemoveRandomFromFiles(self):
        # randomm = randrange(len(self.files) - 1)
        randomm = random.randint(0,len(self.files) - 1)
        self.files.pop(randomm)
        print(randomm)
        iteration = self.currentiteration + 1
        self.currentiteration= iteration
        
    def GetOutputPath(self, file):
        basee = os.path.basename(file)
        outputpath = os.path.join(self.opt.output, basee)
        return outputpath
        
    def CheckFileExists(self, file):
        outputpath = self.GetOutputPath(file)
        return os.path.exists(outputpath)

    def ProcessCurrentFile(self):
        randomm = randrange(len(self.files) - 1)
        if self.opt.random_shot == False:
            randomm = self.currentindex + 1
        self.currentindex = randomm
        if randomm not in self.copied:
            self.copied.append(randomm)
            if not self.CheckFileExists(self.files[randomm]):
                outputpath = self.GetOutputPath(self.files[randomm])
            # print("File Exists : ",self.files[randomm], self.CheckFileExists(self.files[randomm]))
                print("Copying | ",self.files[randomm])
                print("Output | ",outputpath)
                shutil.copy(self.files[randomm], outputpath)
                iteration = self.currentiteration + 1
                self.currentiteration= iteration
                
        # else:
            # remedialiteration = self.currentiteration - 1
            # self.currentiteration= remedialiteration
            

    
    def ProcessFiless(self):
        self.currentiteration = 0
        while self.currentiteration < self.shoutCount:
        # for self.currentiteration in range(0, self.shoutCount):
            print("-----------------------------------------------------------------------------------------------------------")
            print("Iteration : ", self.currentiteration)
            print("-----------------------------------------------------------------------------------------------------------")
            self.RemoveRandomFromFiles()
            # self.ProcessCurrentFile()

if __name__ == '__main__':
    cop = CopyFilesToDirectory()
    cop.ProcessFiless()