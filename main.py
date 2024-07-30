from moviepy.editor import VideoFileClip, vfx


def change_video_duration_and_size(input_path, output_path, target_duration=None, target_resolution=None, min_fps=20):
    # Load the video
    clip = VideoFileClip(input_path)

    # Adjust the duration
    if target_duration:
        original_duration = clip.duration
        if target_duration > original_duration:
            # Extend the duration by lowering the FPS or duplicating frames
            new_fps = max(min_fps, clip.fps * original_duration / target_duration)
            clip = clip.set_fps(new_fps).fx(vfx.loop, duration=target_duration)
        else:
            # Shorten the duration by increasing the FPS or deleting frames
            new_fps = min(clip.fps * original_duration / target_duration, clip.fps * 2)
            clip = clip.set_fps(new_fps).subclip(0, target_duration)

    # Adjust the resolution
    if target_resolution:
        clip = clip.resize(target_resolution)

    # Save the new video
    clip.write_videofile(output_path, codec='libx264')


# Example usage
change_video_duration_and_size('example.mp4', 'output.mp4', target_duration=5, target_resolution=(640, 480))
