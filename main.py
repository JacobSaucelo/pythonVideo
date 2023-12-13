from moviepy.editor import VideoFileClip

clip = VideoFileClip("vidTemplate.mp4")

clip = clip.subclip(0, 15)

resizedVideo = clip.resize((100,144))
resizedVideo.write_videofile("clip.mp4")