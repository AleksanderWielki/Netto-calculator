import sys


brutto = []

if(len(sys.argv) < 7):
    print("Please give 6 arguments")

for i in sys.argv:
    if(i != __file__):
        brutto.append(i)
    

