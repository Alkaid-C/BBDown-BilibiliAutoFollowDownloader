import subprocess
import pathlib
import shlex
import tempfile
import multiprocessing 
import csv
import os
import time
import sys
from datetime import datetime


TempDir=r".\BBDown\data\temp"
RecordDir=r".\BBDown\data\record"
BBDownPath=r".\BBDown\bin\bbdown.exe"
FFprobePath=r".\ffmpeg\ffprobe.exe"
CachePath=r"E:\BiliBiliCache\Cache"
FollowListPath=r".\BBDown\Followlist.txt"
DownloadPath=r"E:\BiliBiliCache"


def Download(VideoLink):
    Command=BBDownPath+r" "+VideoLink +" --work-dir "+CachePath+r" > nul 2>&1"
    os.system(Command)
    
def isLandscape(videoPath):
    probePath = pathlib.PureWindowsPath(FFprobePath).as_posix()
    videoPath = pathlib.PureWindowsPath(FFprobePath).as_posix()
    cmd =r'"'+probePath+r'" -v error -select_streams v -show_entries stream=width,height -of csv=p=0:s=x "'+videoPath+r'"'
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd, stdout=tempf)
        proc.wait()
        tempf.seek(0)
        resolution=tempf.read().decode();

    width=resolution.split("x")[0]
    height=resolution.split("x")[1].split('\\')[0]
    return height<=width

def flatten(workDir,rootDir):
    ContentList=os.listdir(workDir)
    for Item in ContentList:
        if not os.path.isfile(os.path.join(workDir,Item)):
            flatten(os.path.join(workDir,Item),workDir)
            os.rmdir(os.path.join(workDir,Item))
        else:
            if not workDir==rootDir:
                prefix=workDir.replace(rootDir,"").replace("\\","-")[1:]+"-"
                newName=prefix+Item
                newPath=os.path.join(rootDir,newName)
                curPath=os.path.join(workDir,Item)
                os.rename(curPath, newPath)
    
def isLandscape(videoPath):
    probePath = pathlib.PureWindowsPath(FFprobePath).as_posix()
    videoPath = pathlib.PureWindowsPath(videoPath).as_posix()
    cmd =r'"'+probePath+r'" -v error -select_streams v -show_entries stream=width,height -of csv=p=0:s=x "'+videoPath+r'"'
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd, stdout=tempf)
        proc.wait()
        tempf.seek(0)
        resolution=tempf.read().decode();

    width=resolution.split("x")[0]
    height=resolution.split("x")[1].split('\\')[0]
    return height<=width
    
def PostDownloadFix(workDir, finalDir):
        flatten(workDir,workDir)
        count = 0
        ContentList=os.listdir(workDir)
        for Item in ContentList:
            videoPath=os.path.join(workDir,Item)
            if not isLandscape(videoPath):
                os.remove(videoPath)
                count+=1
        NewVideos = os.listdir(workDir)
        for video in NewVideos:
            os.rename(os.path.join(workDir,video),os.path.join(finalDir,video))
        print(r"Deleted "+str(count)+r" portrait videos.")
                

def RecordFormatter(MID):
    MIDtxt=MID+(r'.txt')
    tempVar = os.listdir(TempDir)
    NewFollowtxt = tempVar[0]
    os.rename(os.path.join(TempDir,NewFollowtxt),os.path.join(TempDir,MIDtxt))
    os.rename(os.path.join(TempDir,MIDtxt),os.path.join(RecordDir,MIDtxt))       
                
def Initializer():
    if not os.path.exists(RecordDir):
        os.makedirs(RecordDir)
    if not os.path.exists(TempDir):
        os.makedirs(TempDir)
    if not os.path.exists(CachePath):
        os.makedirs(CachePath)
    if not os.path.exists(DownloadPath):
        os.makedirs(DownloadPath)
    if not os.path.exists(FFprobePath):
        print(r"error: ffprobe.exe not found, disable postDownloadFix or edit path varible")
        os.system("PAUSE")
    if not os.path.exists(BBDownPath):
        print(r"error: BBDown.exe not found, edit path variable")
        os.system("PAUSE")
    if not os.path.exists(FollowListPath):
        print(r"error: Followlist.txt not found, edit path variable")
        os.system("PAUSE")
    Trashlist=os.listdir(TempDir)
    for Trash in Trashlist:
        os.remove(os.path.join(TempDir, Trash))
        Trashlist=os.listdir(CachePath)
    for Trash in Trashlist:
        os.remove(os.path.join(CachePath, Trash))
    FollowListFile = open(FollowListPath, encoding="utf8")
    FollowList = FollowListFile.read().splitlines()
    FollowListFile.close()
    CurFileList = os.listdir(RecordDir)
    NewFollowList=[]
    Rewrite=False
    MIDList=[]
    for Line in FollowList:
        MID=Line.split(r",")[0]
        MIDList.append(MID)
        MIDtxt=MID+(r'.txt')
        if MIDtxt not in CurFileList:
            Command=BBDownPath+r" https://space.bilibili.com/"+MID+r" --work-dir "+TempDir+r" > nul 2>&1"
            os.system(Command)
            # to format the new record file and moves it
            time.sleep(0.1)
            Name = os.listdir(TempDir)[0].replace(r"的投稿视频.txt","")
            RecordFormatter(MID)
            NewFollowList.append(MID+r", "+Name)
            Rewrite=True
        else:
            NewFollowList.append(Line)
    for MIDtxt in CurFileList:
        # clean for no longer followed video record
        if MIDtxt.replace(r".txt","") not in MIDList:
            os.remove(os.path.join(RecordDir,MIDtxt))


def GetDownLoadList():
    DownloadList = []
    AllCurRecords = os.listdir(RecordDir)
    for Recordtxt in AllCurRecords:
        MID=Recordtxt.replace(r".txt","")
        CurRecord = open(os.path.join(RecordDir, Recordtxt), encoding="utf8")
        CurVideoList = CurRecord.read().splitlines()
        CurRecord.close()
        Command=BBDownPath +r" https://space.bilibili.com/"+MID+r" --work-dir "+TempDir+r" > nul 2>&1"
        os.system(Command)
        tempVar = os.listdir(TempDir)
        NewRecordtxt = tempVar[0]
        NewRecord = open(os.path.join(TempDir, NewRecordtxt), encoding="utf8")
        NewVideoList = NewRecord.read().splitlines()
        NewRecord.close()
        Existing = False
        i = 0 
        while Existing == False:
        # comparing the new video list with the WHOLE old list, in case the newest one in old list was deleted.
            if NewVideoList[i] not in CurVideoList:
                DownloadList.append(NewVideoList[i])
                if i<len(NewVideoList):
                    i+=1
                else:
                    print("ERROR: Cannot Get New Video For "+MID)
                    os.system("PAUSE")
            else:
                Existing = True
                # it assumes that, at least one video in the new list will appear in the old list. If the assumption fails then this program will crash.
        # to replace the old list by the new list. The replacement is alaways executed even in case two lists are identical to reduce programming complexity.
        os.remove(os.path.join(RecordDir,Recordtxt))
        RecordFormatter(MID)
    return DownloadList
    
def currentTime():
    return datetime.now().strftime(r"[%m/%d %H:%M:%S]")
    
def main():
    print(currentTime()+r" Start initializaton...")
    Initializer()
    print(currentTime()+r" Initialization finisted.")
    print(currentTime()+r" Start retrieving Video list...")
    DownloadList=GetDownLoadList()
    print(currentTime()+r" Retrieval finished. "+str(len(DownloadList))+r" videos to download.")
    print(currentTime()+r" Start downloading...")
    i=1
    for VideoLink in DownloadList:
        print(currentTime()+r"Download: "+str(i)+r"/"+str(len(DownloadList)))
        av=VideoLink.replace(r"https://www.bilibili.com/video/", "")
        Download(VideoLink)
        i+=1
    print(currentTime()+r" Download finished.")
    print(currentTime()+r" Start fixing...")
    PostDownloadFix(CachePath,DownloadPath)
    print(currentTime()+r" Fix finished.")
    os.system("PAUSE")

main()
    
    
    

