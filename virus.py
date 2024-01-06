import subprocess
import random
limrq=open("LIMIT.txt","r")
limit=str(limrq.read())
if not limit=="0":
  limit=int(limit)
  print("limit not false, limit:", limit)
  nameunique=False
  limwrite=open("LIMIT.txt","w")
  limwrite.write(str(int(limit)-1))
  r = random.randint(1, 9999999999)
  filen = str(r) + ".py"
  while nameunique==False:
    try:
      p=open(filen,"x")
    except:
      print("failed")
    else:
      nameunique=True  
  print(__file__)
  curflnm=__file__
  curfl=open(curflnm,"r")
  nextfl=open(filen,"w")
  nextfl.write(str(curfl.read()))
  subprocess.run(filen,shell=True)
  