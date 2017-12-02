import requests,os
list = ['maxresdefault','hqdefault','sddefault','default','1','2','3']
def createDir(name):
	try:
		if not os.path.exists(name):
			os.makedirs(name)
	except OSError:
		print("Can Not Create Directory")
	os.chdir(name)

def yt(url):
	url = url.split('=')
	createDir(url[1])
	for names in list:
		imgUrl = "https://img.youtube.com/vi/"+url[1]+"/"+names+".jpg"
		rawImage = requests.get(imgUrl)
		with open(names+'.jpg','wb') as dn:
			dn.write(rawImage.content)

if __name__ == '__main__':
	url = input("Enter yt Video Url:")
	yt(url)
	# print("Youtube Thumbnail Downloaded Sucessfully.")
		




