import os


def Initializer():
    FollowListFile = open(r'Followlist.txt', "r")
    FollowList = FollowListFile.read().splitlines()
    ExistingFollow = os.listdir(r".\BBDown\New_AV_List")
    if len(FollowList)>len(ExistingFollow):
        print(r"Initialize for new follow...No video will be downloaded from new follow.")
        for x in range (len(FollowList)-len(ExistingFollow)):
            Command=r".\BBDown\BBDown "+FollowList[x]+r" --work-dir .\BBDown\New_AV_List >nul"
            os.system(Command)
            mid=FollowList[x].replace(r"https://space.bilibili.com/","").replace(r"/video","")
            print(r"Initialize for mid="+  mid +r"...")
    print(r"Initialization Finished.")

def GetDownloadList():
    DownloadList = []
    NewDir=r".\BBDown\New_AV_List"
    CurrentDir=r".\BBDown\Cur_AV_List"
    AllCurLists = os.listdir(NewDir)
    AllTrashLists = os.listdir(CurrentDir)
    FollowListFile = open(r'Followlist.txt', "r")
    FollowList = FollowListFile.read().splitlines()
    for List in AllTrashLists:
        os.remove(os.path.join(CurrentDir, List))
    for List in AllCurLists:
        src_path = os.path.join(NewDir, List)
        dst_path = os.path.join(CurrentDir, List)
        os.rename(src_path, dst_path)
    print(r"Refesh video list...")
    for UpUrl in FollowList:
        mid=UpUrl.replace(r"https://space.bilibili.com/","").replace(r"/video","")
        print(r"Geting video list for mid="+  mid +r"...")
        Command=r".\BBDown\BBDown "+UpUrl+r" --work-dir .\BBDown\New_AV_List >nul"
        os.system(Command)
    CurrentLists = os.listdir(CurrentDir)
    NewLists = os.listdir(NewDir)
    print("Comparing...")
    for List in NewLists:
        NewListPath = os.path.join(NewDir,List)
        NewList = open(NewListPath, "r")
        NewVideoList = NewList.read().splitlines()
        CurListPath = os.path.join(CurrentDir,List)
        CurList = open(CurListPath, "r")
        CurVideoList = CurList.read().splitlines()
        Existing = False
        i = 0 
        while Existing == False:
            if CurVideoList.count(NewVideoList[i])==0:
                DownloadList.append(NewVideoList[i])
                i+=1
            else:
                Existing = True
    for CurList in CurrentLists:
        os.remove(os.path.join(CurrentDir, CurList))
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
