from pytube import YouTube

youtube_video_url = input("Enter video link here:")

try:
    yt_obj = YouTube(youtube_video_url)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    # set output path
    output_path = input("Enter output path:")
    # download the highest quality video
    filters.get_highest_resolution().download(output_path)
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
