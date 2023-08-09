import os

def line_prepender(filename, line):
    # this function is copied from following link, I dont understand it but it runs.
    # https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def RecordFormatter(MID):
    TempDir = r".\BBdown\Temp"
    MIDtxt=MID+(r'.txt')
    tempVar = os.listdir(TempDir)
    NewFollowtxt = tempVar[0]
    os.rename(os.path.join(TempDir,NewFollowtxt),os.path.join(TempDir,MIDtxt))
    line_prepender(os.path.join(TempDir,MIDtxt),NewFollowtxt.replace(r"的投稿视频.txt",""))
    os.rename(os.path.join(TempDir,MIDtxt),os.path.join(r".\BBdown\VideoRecords",MIDtxt))
    
    
def Initializer():
    if not os.path.exists(r".\BBDown\VideoRecords"):
        os.makedirs(r".\BBDown\VideoRecords")
    if not os.path.exists(r".\BBDown\Temp"):
        os.makedirs(r".\BBDown\Temp")
    print(r"Initializing for new follow...No video will be downloaded from new follow.")
    FollowListFile = open(r'Followlist.txt', "r")
    FollowList = FollowListFile.read().splitlines()
    FollowListFile.close()
    CurFileList = os.listdir(r".\BBDown\VideoRecords")

    for MID in FollowList:
        # check if there is new item in followlist and initialize video record for new item
        MIDtxt=MID+(r'.txt')
        if MIDtxt not in CurFileList:
            # to get video record
            Command=r".\BBDown\BBDown https://space.bilibili.com/"+MID+r" --work-dir .\BBDown\Temp >nul"
            os.system(Command)
            print(r"Initializing for mid="+ MID +r"...")
            # to format the new record file and moves it
            RecordFormatter(MID)
           
    for MIDtxt in CurFileList:
        # clean for no longer followed video record
        if MIDtxt.replace(r".txt","") not in FollowList:
            print(r"Removing record for mid="+ MID +r"...")
            os.remove(os.path.join(r".\BBDown\CurVideoRecords",MIDtxt))

    print(r"Initialization finished.")

def GetDownloadList():
    # to clean trash in temp folder in case the program crashed last time
    Trashlist=os.listdir(r".\BBdown\Temp")
    for Trash in Trashlist:
        os.remove(os.path.join(r".\BBdown\Temp", Trash))
    print(r"Refesh video list...")
    DownloadList = []
    RecordDir=r".\BBDown\VideoRecords"
    AllCurRecords = os.listdir(RecordDir)
    for Recordtxt in AllCurRecords:
        MID=Recordtxt.replace(r".txt","")
        CurRecord = open(os.path.join(RecordDir, Recordtxt), "r")
        CurVideoList = CurRecord.read().splitlines()
        CurRecord.close()
        print(r"Getting new video list for "+ CurVideoList[0]+", mid="+MID+"...")
        Command=r".\BBDown\BBDown https://space.bilibili.com/"+MID+r" --work-dir .\BBDown\Temp >nul"
        os.system(Command)
        tempVar = os.listdir(r".\BBdown\Temp")
        NewRecordtxt = tempVar[0]
        NewRecord = open(os.path.join(r".\BBdown\Temp", NewRecordtxt), "r")
        NewVideoList = NewRecord.read().splitlines()
        NewRecord.close()
        Existing = False
        i = 0 
        while Existing == False:
        # comparing the new video list with the WHOLE old list, in case the newest one in old list was deleted.
            if NewVideoList[i] not in CurVideoList:
                DownloadList.append(NewVideoList[i])
                i+=1
            else:
                Existing = True
                # it assumes that, at least one video in the new list will appear in the old list. If the assumption fails then this program will crash.
        # to replace the old list by the new list. The replacement is alaways executed even in case two lists are identical to reduce programming complexity.
        os.remove(os.path.join(RecordDir,Recordtxt))
        RecordFormatter(MID)
    return DownloadList

def Download(VideoLink):
    Command=r".\BBDown\BBDown "+VideoLink+r" >nul"
    os.system(Command)


def main():
    Initializer()
    DownloadList=GetDownloadList()
    print(r"Start Downloading...Downloading "+str(len(DownloadList))+" videos...")
    for VideoLink in DownloadList:
        av=VideoLink.replace(r"https://www.bilibili.com/video/", "")
        print(r"Downloading "+  av+ " ...")
        Download(VideoLink)
    print(r'We have downloaded the following video(s):')
    print(DownloadList)
    os.system("PAUSE")
       
main()
