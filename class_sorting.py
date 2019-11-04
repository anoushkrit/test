import os
import csv
import pandas as pd
import cv2
import shutil


def img_size_csv(path):
    with open('dimensions.csv', 'w') as f:
        for folderName, subFolders, fileNames in os.walk(path):
            for filename in fileNames:
                try:
                    size = os.path.getsize(os.path.join(folderName, filename))
                    img = cv2.imread(os.path.join(folderName, filename))
                    height, width, channels = img.shape
                    df = {"Name": filename, "Height": height, "Width": width, "Channels": channels, "Size": size}
                    # df.append(df)

                    w = csv.DictWriter(f, df.keys())
                    w.writerow(df)
                except:
                    continue
    return



CSV_FILE = ""
SOURCE_PATH = ""
DEST_PATH = ""


def select_data_extract(csv_file, source_path, dest_path):
    mkdir = input("Do you want to make folders?")
    if mkdir == "1":
        os.mkdir(dest_path + "/" + "1")
        os.mkdir(dest_path + "/" + "2")
        os.mkdir(dest_path + "/" + "3")
        os.mkdir(dest_path + "/" + "4a")
        os.mkdir(dest_path + "/" + "4b")
        os.mkdir(dest_path + "/" + "4c")
        os.mkdir(dest_path + "/" + "5")

    df = pd.read_csv(csv_file)
    for folderName, subFolders, fnames in os.walk(source_path):
        for fname in fnames:
            if fname.endswith('.png') | fname.endswith('.jpg'):
                if fname == df.filename[df['filename']]:
                    try:
                        img = cv2.imread(os.path.join(folderName, fname))
                        crop_img = img[df['y1']: df['y2'], df['x1']:df['x2']]
                        cv2.imwrite(dest_path + "/" + df.BIRADs[df['BIRADs']] + "/" + df.filename[df['filename']], crop_img)
                        shutil.copy(os.path.join(folderName, fname), dest_path + "/" + df.BIRADs[df['BIRADs']])
                    except:
                        continue


select_data_extract(csv_file=CSV_FILE, source_path=SOURCE_PATH, dest_path=DEST_PATH)