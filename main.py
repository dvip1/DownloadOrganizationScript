#organizing download directory 
import os 
import shutil

source = r'C:\Users\dvipa\Downloads'

pdf_directory = r'C:\Users\dvipa\Downloads\PDF'
image_directory = r'C:\Users\dvipa\Downloads\Images'
video_directory = r'C:\Users\dvipa\Downloads\Videos'
audio_directory = r'C:\Users\dvipa\Downloads\Audio'
software_directory = r'C:\Users\dvipa\Downloads\Software'
text_directory = r'C:\Users\dvipa\Downloads\Text'
compressed_directory = r'C:\Users\dvipa\Downloads\Compressed'
docs= r'C:\Users\dvipa\Downloads\Docs'
other_directory = r'C:\Users\dvipa\Downloads\Other'

pdf_extensions = ('.pdf')
image_extensions = ('.jpg', '.png', '.jpeg', '.gif', '.bmp', '.svg')
video_extensions = ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg')
audio_extensions = ('.mp3', '.wav', '.ogg', '.aac', '.flac')
software_extensions = ('.exe', '.pkg', '.dmg', '.msi')
text_extensions = ('.txt', '.doc', '.docx', '.odt', '.pdf', '.rtf')
compressed_extensions = ('.zip', '.rar', '.tar', '.gz', '.7z')
docs_extensions = ('.doc', '.docx', '.odt', '.pdf', '.rtf')

for file in os.listdir(source):
    filename, extension = os.path.splitext(file)
    if extension in pdf_extensions:
        if not os.path.exists(pdf_directory):
            os.makedirs(pdf_directory)
        shutil.move(source + '/' + file, pdf_directory)
    elif extension in image_extensions:
        if not os.path.exists(image_directory):
            os.makedirs(image_directory)
        shutil.move(source + '/' + file, image_directory)
    elif extension in video_extensions:
        if not os.path.exists(video_directory):
            os.makedirs(video_directory)
        shutil.move(source + '/' + file, video_directory)
    elif extension in audio_extensions:
        if not os.path.exists(audio_directory):
            os.makedirs(audio_directory)
        shutil.move(source + '/' + file, audio_directory)
    elif extension in software_extensions:
        if not os.path.exists(software_directory):
            os.makedirs(software_directory)
        shutil.move(source + '/' + file, software_directory)
    elif extension in text_extensions:
        if not os.path.exists(text_directory):
            os.makedirs(text_directory)
        shutil.move(source + '/' + file, text_directory)
    elif extension in compressed_extensions:
        if not os.path.exists(compressed_directory):
            os.makedirs(compressed_directory)
        shutil.move(source + '/' + file, compressed_directory)
    else:
        if not os.path.exists(other_directory):
            os.makedirs(other_directory)
        shutil.move(source + '/' + file, other_directory)