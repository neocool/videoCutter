from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

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
    
    # Extract the current part from the long video using ffmpeg
    ffmpeg_extract_subclip("data/v1.mp4", start_time, end_time,
                           targetname=f"data/output/DeadSpace_part_{i+1}.mp4")
