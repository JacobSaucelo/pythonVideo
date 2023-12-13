from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import crop

clip = VideoFileClip("vidTemplate.mp4")

clip = clip.subclip(0, 15)
(w,h) = clip.size


cropClip = crop(clip, width=70, height=144, x_center=w/2, y_center=h/2)
finalClip = cropClip.resize(width=100)

finalClip.write_videofile("clip.mp4")