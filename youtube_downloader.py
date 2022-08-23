import pytube

print("Enter Video url")
url = input(":>> ")

#print("Enter path for storage")
#path = input(":>> ")

#specifying the storage path of the video, either path can be used
path = "E:"

#main code line to download the video
pytube.Youtube(url).streams.get_highest_resolution().download(path)