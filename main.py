import youtube_dl
import pandas as pd
import librosa
import numpy as np

## Input of video link
url = input("Enter video's link :")

## for downloading audio
audio_opts = {
    
    'format': '251',## to change refer to https://github.com/ytdl-org/youtube-dl#format-selection
    #'quiet':True, ## to hide metadata
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredquality': '192',
    }],
    'restrictfilenames':True,
    'forcefilename':True,
    'outtmpl':'/dataset/audio_%(id)s.opus',
    
}
#print('https://www.youtube.com/watch?v=ODm-DmMW31k is 11Hour','https://www.youtube.com/watch?v=02I5vVxlJhU is 81mins',sep='\n')

## Download Audio
with youtube_dl.YoutubeDL(audio_opts) as ydl:
    ydl.download([url])
    info_dict = ydl.extract_info(url, download=False)
    audio_name = ydl.prepare_filename(info_dict)
    #print(audio_name)

## for downloading video
video_opts = {
    
    'format': '18',## to change refer to https://github.com/ytdl-org/youtube-dl#format-selection
    #'quiet':True, ## to hide metadata
    'outtmpl':'/dataset/video_%(id)s.%(ext)s',
    
}
#print('https://www.youtube.com/watch?v=ODm-DmMW31k is 11Hour','https://www.youtube.com/watch?v=02I5vVxlJhU is 81mins',sep='\n')
## Download video 
with youtube_dl.YoutubeDL(video_opts) as ydl:
    ydl.download([url])
    info_dict = ydl.extract_info(url, download=False)
    video_name = ydl.prepare_filename(info_dict)
    #print(video_name)

## x -> audio data
## sr -> sample rate
x, sr = librosa.load(audio_name)

## Creating a 5 second window of data
max_slice=5 
window_length = max_slice * sr

## Audience energy from the tournament to select clip
energy = np.array([sum(abs(x[i:i+window_length]**2)) for i in range(0, len(x), window_length)])
energy = np.sort(energy)

## To analyse energy's frquency
#import matplotlib.pyplot as plt 
#plt.hist(energy) 
#plt.show()
#plt.boxplot(energy)
#plt.show()

## Dataframe for analysing
df=pd.DataFrame(columns=['energy','start','end'])
thresh=np.median(energy[int(energy.shape[0]/2):])
row_index=0
for i in range(len(energy)):
  value=energy[i]
  if(value>=thresh):
    i=np.where(energy == value)[0]
    df.loc[row_index,'energy']=value
    df.loc[row_index,'start']=i[0] * 5
    df.loc[row_index,'end']=(i[0]+1) * 5
    row_index= row_index + 1

## Merging continous clips
temp=[]
i=0
j=0
n=len(df) - 2
m=len(df) - 1
while(i<=n):
  j=i+1
  while(j<=m):
    ## if nth clip's ending is (n+1)th clip's starting
    if(df['end'][i] == df['start'][j]):
      ## replace nth end with (n+1)th end
      df.loc[i,'end'] = df.loc[j,'end']
      temp.append(j)
      j=j+1
    else:
      i=j
      break  
df.drop(temp,axis=0,inplace=True)

## Extracts video's highlight
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start=np.array(df['start'])
end=np.array(df['end'])
for i in range(len(df)):
 if(i!=0):
  start_lim = start[i] - 5
 else:
  start_lim = start[i] 
 end_lim   = end[i]   
 filename="output/highlight" + str(i+1) + ".mp4"
 ffmpeg_extract_subclip(video_name,start_lim,end_lim,targetname=filename)

