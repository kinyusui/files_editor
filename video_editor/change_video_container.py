import os
import ffmpeg
from tkinter import filedialog as fd


def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file
        ).output(out_name,
        vcodec="copy",
        acodec="copy",
        scodec="copy",
        ).run()
    print("Finished converting {}".format(mkv_file))

def change_all_in_directory(start_dir):
    for path, folder, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.mkv'):
                print("Found file: %s" % file)
                convert_to_mp4(os.path.join(start_dir, file))
            else:
                pass

start_dir = fd.askdirectory()
change_all_in_directory(start_dir)