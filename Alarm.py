#!/usr/bin/python

import mpd
from Fade import fade

def alarm(interface,fadeTime,song=None):
	"""starts playback and fades in for [fadeTime] seconds"""
	client=mpd.MPDClient()
	client.connect(interface.host,interface.port)

	endVol=int(client.status()["volume"])

	index=None
	
	if(song):
		# add the song to the queue
		print("alarm: adding song "+song)
		index=client.addid(song)

	if(endVol>0):
		client.setvol(0)

		print("alarm: starting playback")
		if(index!=None):
			client.playid(index)
		else:
			client.play()
		
		fade(client,fadeTime,0,endVol)
	else:
		print("Volume not available, skipping fade.")

		print("alarm: starting playback")
		if(index!=None):
			client.playid(index)
		else:
			client.play()

	client.close()
