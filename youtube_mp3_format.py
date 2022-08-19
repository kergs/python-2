from pytube import YouTube
import os

#url input from user
yout = YouTube(str(input("Enter the URL of the Video you to download\n:>>"))) 

#extracting audio
video = yout.streams.filter(only_audio=True).first()

#destination to save file
print("Enter the destination (leave blank)")
destination = str(input(":>>"))

#downloading the file
out_file = video.download(out_path=destination)

#save file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

#result 
print(yout.title + " has been successfully downloaded in mp3 format.")