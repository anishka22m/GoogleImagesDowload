#Find the package on pypi.org 
#install the package using pip command on CMD
#import the package function and use to download bulk google images

from pygoogle_image import image as pi
KW = input("Enter keyword to download images:")
limter = int(input("Enter how many images you want to download: "))
pi.download(keywords=KW , limit=limter)
