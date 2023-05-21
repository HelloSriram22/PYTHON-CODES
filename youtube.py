from pytube import YouTube

link = "https://www.youtube.com/watch?v=FYIDBhtSuzw"
YouTube_1 = YouTube(link)

# Uncomment the following lines if you want to print video title and thumbnail URL
# print(YouTube_1.title)
# print(YouTube_1.thumbnail_url)

videos = YouTube_1.streams.all()
vid = list(enumerate(videos))

for i in vid:
    print(i)

print()
strm = int(input("Enter the number corresponding to the desired video quality: "))
videos[strm].download()
print("Download successful.")
