from pytube import YouTube
from pytube import Search
from pytube import __title__
import pandas as pd


def search_results(video_name):
    # searching for the video in youtube
    result = Search(video_name)
    print(f"{len(result.results)} have been found ")
    # storing the video and link in a dictionary
    video_dict = {"video": [], "link": []}
    i = 1
    for video in result.results:
        print(f"{i} {video.title} - {video.watch_url}\n")
        video_dict["video"].append(video.title)
        video_dict["link"].append(video.watch_url)
        i += 1
    # to allow the user to choose which video to download from the search results
    print("\n\n Enter the number of the video you want to download")
    number = int(input())
    video_download(number, video_dict)
    return


# for downloading the video in best possible resolution
def video_download(number, video_dict):
    video = YouTube(video_dict["link"][number - 1])
    print("Downloading................. ")
    video.streams.get_highest_resolution().download()
    print("download complete.................")


def main():
    video_name = "sakkigoni"
    search_results(video_name)


if __name__ == "__main__":
    main()
