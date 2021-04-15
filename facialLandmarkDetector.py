
import dlib,cv2
import numpy as np
from renderFace import renderFace
from scipy.spatial import distance as dist

def writeLandmarksToFile(landmarks, landmarksFileName):
  coords=[]
  i=0

  with open(landmarksFileName, 'w') as f:
    for p in landmarks.parts():
      if i in range(36,42):
        # f.write("%s %s\n" %(int(p.x),int(p.y)))
        coords.append([int(p.x),int(p.y)])

      if i in range(42,48):
        coords.append([int(p.x),int(p.y)])
      i+=1

  f.close()
  return coords
def shape_to_np(shape, dtype="int"):
  # initialize the list of (x, y)-coordinates
  coords = np.zeros((68, 2), dtype=dtype)
 
  # loop over the 68 facial landmarks and convert them
  # to a 2-tuple of (x, y)-coordinates
  for i in range(0, 68):
    coords[i] = (shape.part(i).x, shape.part(i).y)
 
  # return the list of (x, y)-coordinates
  return coords

# Landmark model location
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
# Get the face detector
faceDetector = dlib.get_frontal_face_detector()
# The landmark detector is implemented in the shape_predictor class
landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)

# Read image
#imageFilename = "hillary_clinton.jpg"
cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 10.0, (640,480))
points=[]
wideness=[]
between=[]
m=0
while 1:

  ret, img = cam.read()
#im= cv2.imread(imageFilename)
# landmarks will be stored in results/family_i.txt
  landmarksBasename = "results/faces"

# Detect faces in the image
  faceRects = faceDetector(img, 0)
  
  #print(len(faceRects))
  """for i in range(len(faceRects)):
    x,y,w,h=faceRects[0].left(),faceRects[0].right(),faceRects[0].top(),faceRects[0].bottom()
    print(x,y,w,h)
  a1=[x,y]
  a2=[x+w,y]
  a3=[x,y+h]
  d1=dist.euclidean(a1,a2)
  d2=dist.euclidean(a1,a3)
  ratio=d2/d1
  print(ratio)"""



  #print("Number of faces detected: ",len(faceRects))



# List to store landmarks of all detected faces
  landmarksAll = []

# Loop over all detected face rectangles
  for i in range(0, len(faceRects)):
    newRect = dlib.rectangle(int(faceRects[i].left()),int(faceRects[i].top()),
      int(faceRects[i].right()),int(faceRects[i].bottom()))

  # For every face rectangle, run landmarkDetector
    landmarks = landmarkDetector(img, newRect)


  # Print number of landmarks
 # if i==0:

    #print("Number of landmarks",len(landmarks.parts()))

  # Store landmarks for current face
  landmarksAll.append(landmarks)


  # Draw landmarks on face
  renderFace(img, landmarks)

  landmarksFileName = landmarksBasename +"_"+ str(i)+ ".txt"
 # print("Saving landmarks to", landmarksFileName)

  # Writelandmarks to disk
  coords= writeLandmarksToFile(landmarks, landmarksFileName)

  for i in coords:
    cv2.circle(img,tuple(i), 1, (0,0,255), 1 )
  left2right=dist.euclidean(coords[6],coords[0]) #0.412
  lefteyewideness=dist.euclidean(coords[3],coords[0])
  righteyewideness=dist.euclidean(coords[1],coords[5])#0.12
  
  EAR1=( (dist.euclidean(coords[1],coords[5])+dist.euclidean(coords[2],coords[4]))/left2right)

  y=(433/48)*left2right-288
  print("y= ",y)
  
  # points.append([ratio,EAR1])
  #EAR1*=1/(1.5*ratio)
  print(EAR1)
  out.write(img)
  m+=1

  wideness.append([m,EAR1])

  cv2.imshow("Facial Landmark detector", img)
 # cv2.draw

  k= cv2.waitKey(10) & 0xff
  if k==27:
      break

      cap.release()



cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np; np.random.seed(2)
import matplotlib.pyplot as plt

xy=wideness
 
##print(xy)

print(xy)
plt.figure()
for i, ((x,y),) in enumerate(zip(xy)):
  if i%10==0:

    plt.text(x,y,"o", ha="center", va="center")
    x,y =zip(*xy)
    plt.scatter(x,y, alpha=0) 


plt.show()
