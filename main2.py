import dlib,cv2
import numpy as np
from renderFace import renderFace
from scipy.spatial import distance as dist
import average_value_assigner as cal
import win32api
import pyautogui
import os   
import winsound
speed=0
stop_con=1
average =0
temp=[]
ratios=[-1]*3
c=0
callibration=True
left_coords=[]
right_coords=[]
iris=[]
temp3=0
temp4=0
temp5=0
iris_average=0
iris_ratios=[]
number_of_iris_coords=[]
frequency = 2500
frequency2 =5000
frequency3=1500
duration = 500 
consecframes2=0

global state_left
state_left = win32api.GetKeyState(0x01)

def iris_mean(iris_r,number_of_iris_coords):

    for i in range(len(number_of_iris_coords)):
        if number_of_iris_coords[i]==3:
            proper_index=2*i
    proper_table=[]
    for i in range(3):
        proper_table.append(iris_r[proper_index+i][0])



    global temp3,temp4,temp5
    for i in range(len(iris_r)):
        if i%3==0:

            if(iris_r[i][0]==-1):
                iris_r[i][0]=proper_table[0]
            temp3+=iris_r[i][0]


        if i%3==1:
            if(iris_r[i][0]==-1):
                iris_r[i][0]=proper_table[1]
            temp4+=iris_r[i][0]

        if i%3==2:
            if(iris_r[i][0]==-1):
                iris_r[i][0]=proper_table[2]
            temp5+=iris_r[i][0]


    temp3=temp3/3
    temp4=temp4/3
    temp5=temp5/3
    temp3=temp3-(temp3/4)
    pass1=1
    pass2=1
    while(pass1 or pass2):
        if temp3-temp4>1.5:
            pass1=0            
        else:
            temp4=temp4-(temp4/5)
        if temp4-temp5>1:
            pass2=0
        else:
            temp5=temp5-(temp5/5)

    iris_ratios=[temp3,temp4,temp5]
    return iris_ratios
def mask(image,roi_corners):
    roi_corners=np.array(roi_corners)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    mask=np.zeros((image.shape[0],image.shape[1]))
    
    #ignore_mask_color=(255)
    cv2.fillPoly(mask,pts=[roi_corners],color=(255,255,255))
    for i in range(len(image)):
        for j in range(len(image[0])):
            #cv2.imshow("mask",mask)
            if (mask[i][j]==255):
                pass
            if (mask[i][j]==0):
                image[i][j]=255
    mask=None
    #cv2.imshow("mask",mask)
    return image
def iris_center(orig):
    #orig=cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)

    orig=cv2.GaussianBlur(orig,(5,5),0)
    orig=cv2.GaussianBlur(orig,(3,3),0)
    minVal,maxVal, minLoc,maxLoc=cv2.minMaxLoc(orig)
    return minLoc


def writeLandmarksToFile(landmarks, landmarksFileName):
  coords=[]
  coords2=[]
  i=0

  with open(landmarksFileName, 'w') as f:
    for p in landmarks.parts():
      if i in range(36,42):
        # f.write("%s %s\n" %(int(p.x),int(p.y)))
        coords.append([int(p.x),int(p.y)])

      if i in range(42,48):
        coords.append([int(p.x),int(p.y)])
      
      if i in (2,14,31,35):
        coords2.append([int(p.x),int(p.y)])
      i+=1  

  f.close()
  return coords,coords2
def mean(a):
    s=0
    for i in range(len(a)):
        s+=a[i]
    return s/len(a)


def shape_to_np(shape, dtype="int"):
  # initialize the list of (x, y)-coordinates
  coords = np.zeros((68, 2), dtype=dtype)
 
  # loop over the 68 facial landmarks and convert them
  # to a 2-tuple of (x, y)-coordinates
  for i in range(0, 68):
    coords[i] = (shape.part(i).x, shape.parte(i).y)
 
  # return the list of (x, y)-coordinates
  return coords

def eyes():
# Landmark model location
    PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
    # Get the face detector
    faceDetector = dlib.get_frontal_face_detector()
    # The landmark detector is implemented in the shape_predictor class
    landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)

    # Read image
    #imageFilename = "hillary_clinton.jpg"
    cam = cv2.VideoCapture(0)
    global temp
    global frequency
    global durationq

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 10.0, (640,480))
    points=[]
    wideness=[]
    between=[]
    m=0
    consecframes=0
    consecframes3=0
    consecframes4=0
    while 1:
        ret, img = cam.read()
    #im= cv2.imread(imageFilename)
    # landmarks will be stored in results/family_i.txt
        landmarksBasename = "results/faces"

    # Detect faces in the image
        faceRects = faceDetector(img, 0)

        # List to store landmarks of all detected faces
        landmarksAll = []

        # Loop over all detected face rectangles
        for i in range(0, len(faceRects)):
            newRect = dlib.rectangle(int(faceRects[i].left()),int(faceRects[i].top()),int(faceRects[i].right()),int(faceRects[i].bottom()))

        # For every face rectangle, run landmarkDetector
        landmarks = landmarkDetector(img, newRect)

        # Store landmarks for current face
        landmarksAll.append(landmarks)


        # Draw landmarks on face
        #renderFace(img, landmarks)

        landmarksFileName = landmarksBasename +"_"+ str(i)+ ".txt"
        # print("Saving landmarks to", landmarksFileName)

        # Writelandmarks to disk
        coords,coords2= writeLandmarksToFile(landmarks, landmarksFileName)
        #print(coords)

        #for i in coords:
            #cv2.circle(img,tuple(i), 1, (0,0,255), 1 )
        left2right=dist.euclidean(coords[6],coords[0]) #0.412
        lefteyewideness=dist.euclidean(coords[3],coords[0])
        righteyewideness=dist.euclidean(coords[1],coords[5])#0.12

        x1=coords[0][0]
        y1=min(coords[1][1],coords[2][1])
        w1=coords[3][0]
        h1=max(coords[4][1],coords[5][1])


        x2=coords[6][0]
        y2=min(coords[7][1],coords[8][1])
        w2=coords[9][0]
        h2=max(coords[10][1],coords[11][1])
        global left_coords
        global right_coords

        for i in range(6):
            right_coords.append([coords[i][0]-x1,coords[i][1]-y1])
            left_coords.append([coords[i+6][0]-x2,coords[i+6][1]-y2])

        #cv2.rectangle(img,(x1,y1),(w1,h1),(255,255,0),1)

        center_right=None
        center_left=None


        eye_crop_right=img[y1:h1,x1:w1]
        eye_crop_right_gray=cv2.cvtColor(eye_crop_right,cv2.COLOR_BGR2GRAY)
        #eye_crop_right_mask=mask(eye_crop_right,right_coords)
        center_right=iris_center(eye_crop_right_gray)
        #cv2.imshow("right",eye_crop_right_mask)
        #print(center_right)
        cv2.circle(eye_crop_right,center_right,5,(0,0,255),2)

        eye_crop_left=img[y2:h2,x2:w2]
        eye_crop_left_gray=cv2.cvtColor(eye_crop_left,cv2.COLOR_BGR2GRAY)
        #eye_crop_left_mask=mask(eye_crop_left,left_coords)
        center_left=iris_center(eye_crop_left_gray)
       #cv2.imshow("left",eye_crop_left_mask)
        ##print(center_left)
        cv2.circle(eye_crop_left,center_left,5,(0,0,255),2)

        #cv2.imshow("crop",eye_crop_left)
        EAR1=( (dist.euclidean(coords[1],coords[5])+dist.euclidean(coords[2],coords[4]))/left2right)


        EAR=( (dist.euclidean(coords[1],coords[5])+dist.euclidean(coords[2],coords[4]))/(2*dist.euclidean(coords[0],coords[3])))



        if callibration == True:
            global average
            global temp3
            global ratios
            global c
            global state_left
            global iris
            global temp3
            global temp4
            global temp5
            global iris_ratios
            global number_of_iris_coords

            a= win32api.GetKeyState(0x01)
            if a != state_left:
                state_left = a
                if average==1:
                    number_of_iris_coords.append(len(temp))
                    ratios[c]=mean(temp)
                    c+=1
                    average=0
                    temp=[]

                if a < 0:
                    if (EAR1):
                        temp.append(EAR1)
                    if(center_right):
                        if (stop_con):
                            iris.append(center_right)
                    else:
                        iris.append([-1,-1])
                    #print(iris)
            if iris_average==1:
                #print("number_of_iris_coords :",number_of_iris_coords)
                iris_ratios=iris_mean(iris,number_of_iris_coords)

        

        #print(ratios)
        if callibration==False:
                #print("ear after callib " ,EAR1)
            cal.callibration(ratios,EAR1,iris_ratios,center_right)
            if EAR1 > ratios[0]+.05 and speed!=0:
                consecframes4+=1
               
             
                if consecframes4>=20 and speed>20:
                    
                    winsound.Beep(frequency3,duration)
            else:
                consecframes4=0
            if EAR < ratios[2]and speed!=0:
                consecframes +=1
                if consecframes >=3:
 # Set Duration To 1000 ms == 1 second
                    winsound.Beep(frequency2, duration)
            else:
                consecframes=0
            if consecframes2>=15 and speed >20:
                winsound.Beep(frequency,duration)
            
            if dist.euclidean(coords2[0],coords2[2])/dist.euclidean(coords2[1],coords2[3])>1.5 or dist.euclidean(coords2[1],coords2[3])/dist.euclidean(coords2[0],coords2[2]) >1.5:
                consecframes3+=1
               
             
                if consecframes3>=20 and speed>20:
                    
                    winsound.Beep(frequency3,duration)
            else:
                consecframes3=0



        out.write(img)
    


        cv2.imshow("Facial Landmark detector", img)
     # cv2.draw

        k= cv2.waitKey(10) & 0xff
        if k==27:
            break

cv2.waitKey(0)
cv2.destroyAllWindows()
