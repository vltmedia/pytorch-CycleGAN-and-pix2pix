# Create a zip file with the checkpoints. Provide the number to the checkpoint you want to zip up

# Example zips up checkpoint 325 files:
# python zipcurrentpoint.py 325 


from zipfile import ZipFile
import os
import sys

checkpointpath = "/content/pytorch-CycleGAN-and-pix2pix/checks/gtavc2city"

filestowrite = ["$F_net_D_A.pth", "$F_net_D_B.pth", "$F_net_G_A.pth", "$F_net_G_B.pth", "latest_net_D_A.pth", "latest_net_D_B.pth", "latest_net_G_A.pth", "latest_net_G_B.pth", "loss_log.txt", "train_opt.txt" ]

numbertocopy = str(sys.argv[1])

def mutateList():
    outlist = []
    for file in filestowrite:
        outpath = os.path.join(checkpointpath, file.replace("$F", numbertocopy))
        if  os.path.exists(outpath):
            print("Exists : ", outpath, os.path.exists(outpath))
            outlist.append(outpath)
    return(outlist)

def ZipFilesInList(filepath, listt):
    
    with ZipFile(filepath,"w") as newzip:
        for file in listt:
            newzip.write(file)
            print("Zipping File : ", file)
    print("Completed zipping files!" , filepath)


def main():
    outlist = mutateList()
    ZipFilesInList("/content/pytorch-CycleGAN-and-pix2pix/checks/gtavc2city/gtavc2city_checkpoint_"+ numbertocopy +"_.zip", outlist)

if __name__ == '__main__':
    main()