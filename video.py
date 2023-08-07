import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.JPEG','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
heigth,width,channels = frame.shape
size = (width,heigth)
print(size)
out = cv2.VideoWriter("Project.avi",cv2.VideoWriter_fourcc(*'DIVX'),1,size)
for i in range(0,count):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()