from pytube import YouTube
import pandas as pd
import os
import csv


def download_video(url, path):
    vid = YouTube(url)
    video = vid.streams.get_highest_resolution()
    if not os.path.exists(path):
        os.makedirs(path)
    if vid == None:
        print("The video does not exist")

    video_info = {"title": vid.title, "url": url}
    df = pd.DataFrame(video_info, index=False)
    df.to_csv("video_info.csv", mode="a", header=False)

    check_video_downloaded("url")
    print("Video has been downloaded")


def check_video_downloaded(url, path):
    df = pd.read_csv("video_info.csv")
    length = len(df["url"])
    for i in length:
        if df["url"][i] == url:
            return
    download_video(url, path)


def main():
    url = input("Enter the URL of the video: ")
    path = "E:/YouTube-Video-Downloader/videos"
    download_video(url, path)


if __name__ == "__main__":
    main()
