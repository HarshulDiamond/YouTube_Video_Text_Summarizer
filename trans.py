from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
vid_id='bSd_juQV5NM'
data=yta.get_transcript(vid_id)
transcript=''
for value in data:
    for key,val in value.items():
         if key == 'text':
              transcript+=val

I= transcript.splitlines()
final_tra=" ".join(I)

file=open("harshul.txt",'w')
file.write(final_tra)
file.close()
