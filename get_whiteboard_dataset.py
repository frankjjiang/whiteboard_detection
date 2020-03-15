import csv
import os

CLASS_LIST = ('/m/02d9qx') # class code from openimages dataset for whiteboard
img_name = "111111111111"

# with open('path\\train-annotations-bbox.csv', newline='') as csvfile:
with open('data/oidv6-train-annotations-bbox.csv', newline='') as csvfile:
    bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for bbox in bboxs:
        if bbox[2] in CLASS_LIST:
            if img_name != bbox[0]:
                if not os.path.isfile("data/whiteboard/%s.jpg"%bbox[0]):
                    # os.system("gsutil cp gs://open-images-dataset/train/%s.jpg destination_path"%bbox[0])
                    os.system("aws s3 --no-sign-request cp s3://open-images-dataset/train/%s.jpg data/whiteboard"%bbox[0])
                    out_file = open("data/whiteboard/%s.txt"%bbox[0], 'w')
                    img_name = bbox[0]
            if img_name == bbox[0]:
                out_file.write(str(CLASS_LIST.index(bbox[2])) + " " + str(float(bbox[4])+(float(bbox[5])-float(bbox[4]))/2) + " " + str(float(bbox[6])+(float(bbox[7])-float(bbox[6]))/2)+ " " + str(float(bbox[5])-float(bbox[4])) + " " + str(float(bbox[7])-float(bbox[6])) + '\n')
