from pytube import YouTube

def download_video(url: str):
    '''Функция загрузки видео с YouTube'''
    try:
        yt = YouTube(url=url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename='video.mp4')
        print('Видео загружено')
        return True
    except Exception as Ex:
        print(Ex)
        return False
