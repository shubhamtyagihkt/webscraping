from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytube import YouTube
driver = webdriver.Firefox()
main_url = "https://www.youtube.com/results?search_query="


def url_download():
    url = input("Enter your video url: ")
    yt = YouTube(url)
    
    if(yt):
        all_qlt = yt.streams.all()
        for q in all_qlt:
            print(q)
        slct = input("Select your quality by 'itag': ")
        stream = yt.streams.get_by_itag(slct)
        print("Your video is being downloaded....")
        stream.download()
        print("Download Complete")



def search_n_download():
    while True:
        word = input("Search your video here: ")
        print('\n')
        query = ('+').join(word.split())
        tube = main_url + query
        driver.get(tube)
        res = driver.execute_script('return document.documentElement.outerHTML')
        soup = BeautifulSoup(res, "lxml")
        driver.quit()
        videos = soup.find_all(class_ ='style-scope ytd-item-section-renderer')
        i = 1; start = 0; end = 0
        for index,video in enumerate(videos):
            title = video.find(id='video-title')
            if(title):
                if(i == 1):
                    start = index
                print(str(i) + '. ' + ' '.join(video.find(id='video-title').text.replace('\n', '').split()))
                i += 1
                end = index
        choice = int(input("\nChoose you video (1~{}): ".format(end-start+1)))
        if choice:
            yt = YouTube(videos[start + choice -1].find('a').get('href'))
            stream = yt.streams.first()
            print("Downlaoding.....")
            print(' '.join(videos[start + choice -1].find(id='video-title').text.replace('\n', '').split()))
            stream.download()
            print("Successfully dowloaded!")
        cont = input("Seach another video? [y/n]: ")
        if(cont == 'n' or cont == 'N' or cont == 'No'):
            break

print("---- Your personal youtube video downloader ---\n")
print("Select the method to DOWNLOAD youtube video: ")
chc = int(input("1. Search Video Online\n2. Download via url\n3. Exit\n\nYour choice: "))
if(chc == 1):
    search_n_download()
elif(chc == 2):
    url_download()
