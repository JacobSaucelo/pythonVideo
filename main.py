from moviepy.editor import *
from moviepy.video.fx.all import crop

clip = VideoFileClip("vidTemplate.mp4")

clip = clip.subclip(0, 15)
(w,h) = clip.size


cropClip = crop(clip, width=70, height=144, x_center=w/2, y_center=h/2)
finalClip = cropClip.resize(width=100)

text = TextClip("hewwo HEEEWWOO", fontsize=14, color="white", bg_color="blue")
# .set_position("center").set_duration(10)

final = CompositeVideoClip([finalClip, text])

final.ipython_display(width = 70)  
# final.write_videofile("clip.mp4")