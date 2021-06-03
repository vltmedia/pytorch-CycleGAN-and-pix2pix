# Cleanup a GAN results folder with _real and _fake files. Will make new folders in the directoy you specify
# sys.argv[1] = Directory to read

import glob
import shutil
import os
import sys
from pathlib import Path




def GetFiles(directory):
    files = glob.glob(directory+'/*.png')
    img_array = []
    temp_array = []
    cleaned_array = []
    for k in files:
    
        img_array.append(k.split("_fake")[0])
        outpath = GetOutputFolder(k,'fake') +'/'+os.path.basename(k.split("_fake")[0]+'_fake.png')
        # print(outpath)
        dictt = {"filepath" : k, "basename" : k.split("_fake")[0], "updatedname" :  outpath, "exportdirectory" :  GetOutputFolder(k,'fake')}
        if k.split("_fake")[0] not in temp_array:
            temp_array.append(k.split("_fake")[0])
            cleaned_array.append(dictt)
        # Path('/content/pytorch-CycleGAN-and-pix2pix/results/gtavc2city/test_latest').mkdir(parents=True, exist_ok=True)
    return cleaned_array


def GetFakeFiles(directory):
    files = glob.glob(directory+'/*fake*.png')
    img_array = []
    temp_array = []
    cleaned_array = []
    filess = [k for k in files if 'real' not in k]
    for k in filess:
    
        img_array.append(k.split("_fake")[0])
        outpath = GetOutputFolder(k,'fake') +'/'+os.path.basename(k.split("_fake")[0]+'_fake.png')
        # print(outpath)
        dictt = {"filepath" : k, "basename" : k.split("_fake")[0], "updatedname" :  outpath, "exportdirectory" :  GetOutputFolder(k,'fake')}
        if k.split("_fake")[0] not in temp_array:
            temp_array.append(k.split("_fake")[0])
            cleaned_array.append(dictt)
        # Path('/content/pytorch-CycleGAN-and-pix2pix/results/gtavc2city/test_latest').mkdir(parents=True, exist_ok=True)
    return cleaned_array

def GetOutputFolder(filepath, typee):
    dirname = os.path.dirname(filepath)
    if typee == 'real':
        if not os.path.exists(os.path.join(dirname, 'real')):
            Path(os.path.join(dirname, 'real')).mkdir(parents=True, exist_ok=True)
        outpath = os.path.join(dirname, 'real')
        return outpath
    if typee == 'fake':
        if not os.path.exists(os.path.join(dirname, 'fake')):
            Path(os.path.join(dirname, 'fake')).mkdir(parents=True, exist_ok=True)
        outpath = os.path.join(dirname, 'fake')
        
        return outpath


def GetRealFiles(directory):
    files = glob.glob(directory+'/*real*.png')
    img_array = []
    temp_array = []
    cleaned_array = []
    filess = [k for k in files if 'fake' not in k]
    for k in filess:
        img_array.append(k.split("_real")[0])
        outpath = GetOutputFolder(k,'real') +'/'+os.path.basename(k.split("_real")[0]+'_real.png')
        # print(outpath)
        dictt = {"filepath" : k, "basename" : k.split("_real")[0], "updatedname" : outpath, "exportdirectory" :  GetOutputFolder(k,'real')}
        if k.split("_real")[0] not in temp_array:
            temp_array.append(k.split("_real")[0])
            cleaned_array.append(dictt)
        # Path('/content/pytorch-CycleGAN-and-pix2pix/results/gtavc2city/test_latest').mkdir(parents=True, exist_ok=True)
    return cleaned_array

def CopyFiles(filearry):
    for filee  in filearry:
        shutil.copy(filee['filepath'],filee['exportdirectory'])
        
def WriteConcacts(filearray):
    templatee = "file '$F'"
    filelist = []
    for filee  in filearray:
        filelist.append(templatee.replace("$F", filee['updatedname']))
    print(sorted(filelist))

def main():
    directory = sys.argv[1]
    files = glob.glob(directory+'/*.png')
    
    # directory = '/content/pytorch-CycleGAN-and-pix2pix/results/gtavc2city/test_latest/images'
    fakefiles = GetFakeFiles(directory)
    realfiles = GetRealFiles(directory)
    if fakefiles != 0:
        # if os.path.exists(os.path.dirname(realfiles[0]['exportdirectory'])):
        #     shutil.rmtree(os.path.dirname(realfiles[0]['exportdirectory']))
        # if os.path.exists(os.path.dirname(fakefiles[0]['exportdirectory'])):
        #     shutil.rmtree(os.path.dirname(fakefiles[0]['exportdirectory']))
        CopyFiles(fakefiles)
        CopyFiles(realfiles)
        # WriteConcacts(fakefiles)
        # WriteConcacts(realfiles)
        
        print("Finished Cleaning Files ")
        print("Real directory: ", os.path.dirname(realfiles[0]['exportdirectory']))
        print("Fake directory : ", os.path.dirname(fakefiles[0]['exportdirectory']))
    else:
        print("(Error: 01120) No Fake Files were generated or found")
    # print(fakefiles[1])
    # print(realfiles[1])
    # print(len(fakefiles))
    # print(len(realfiles))
if __name__ == '__main__':    
    main()
