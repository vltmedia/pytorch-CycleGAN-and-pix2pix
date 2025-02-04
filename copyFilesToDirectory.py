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
        self.opt = UtilOptions().parse()
        
        self.inputDirectory = self.opt.dataroot
        self.outputDirectory = self.opt.output
        self.extension = self.opt.extension
        self.shoutCount = self.opt.shot_count
        self.files = glob.glob(self.opt.dataroot+'/*.'+self.opt.extension)
        self.copied = []
        self.currentindex = 0
        self.ispossible = self.opt.shot_count < len(self.files)
        
        if not self.ispossible:
            self.ShowNotPossibleError()
        print(self.opt)
        
    def ShowNotPossibleError(self):
        print("Error (01002): NOT ENOUGH FILES IN FOLDER TO MATCH REQUESTED SHOT COUNT! TURN YOUR SHOT COUNT DOWN! Shot Count:" + str(self.opt.shot_count) +" > Files Count:"+  str(len(self.files)) )
        
    def CheckIfPossible(self):
        return self.opt.shot_count < len(self.files)
    
    def RemoveRandomFromFiles(self):
        # randomm = randrange(len(self.files) - 1)
        
        randomm = random.randint(0,len(self.files) - 1)
        self.files.pop(randomm)
        iteration = self.currentiteration + 1
        self.currentiteration= iteration
        
    def CopyFilesArray(self):
        for filee in self.files:
            if not self.CheckFileExists(filee):
                outputpath = self.GetOutputPath(filee)
                shutil.copy(filee, outputpath)
                
            
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
        if self.CheckIfPossible():
            self.currentiteration = 0
            while self.currentiteration < self.shoutCount:
            # for self.currentiteration in range(0, self.shoutCount):
                print("-----------------------------------------------------------------------------------------------------------")
                print("Iteration : ", self.currentiteration)
                print("-----------------------------------------------------------------------------------------------------------")
                # self.RemoveRandomFromFiles()
                self.ProcessCurrentFile()
        else:
            self.ShowNotPossibleError()

if __name__ == '__main__':
    cop = CopyFilesToDirectory()
    cop.ProcessFiless()