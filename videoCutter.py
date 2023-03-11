import moviepy.editor as mp

# Define the duration of each part (in seconds)
part_duration = 870

# Load the long video
video = mp.VideoFileClip("data/v1.mp4")

# Get the total duration of the video (in seconds)
total_duration = video.duration

# Calculate the number of parts needed
num_parts = int(total_duration / part_duration) + 1

# Cut the video into parts
for i in range(num_parts):
    # Define the start and end times for the current part
    start_time = i * part_duration
    end_time = min((i + 1) * part_duration, total_duration)
    
    # Extract the current part from the long video
    part = video.subclip(start_time, end_time)
    
    # Save the current part to a new video file
    part.write_videofile(f"data/output/video_part_{i+1}.mp4")


