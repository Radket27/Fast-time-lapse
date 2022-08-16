def file_transport():
    """
    Convert argv into array
    """
    from sys import argv
    name = []
    if(len(argv) == 1):
        print("Set arguments")
        exit()
    for i in range(len(argv)):
        if(i == 0):
            pass
        else:
            name.append(argv[i])
    return name

def clip_make(name,fps,clip_name):
    """
    Create video
    """
    from moviepy.editor import ImageSequenceClip, VideoFileClip
    video = ImageSequenceClip(name,fps)
    video.write_videofile(clip_name)
    return 0

def main():
    """
    Main function
    """
    name = file_transport()
    sort1 = input("sort?(y)\n: ")
    if(sort1 == 'y'):
        name.sort()    
    fps = int(input("Set fps\n: "))
    clip_name = str(input("Set clip name\n: "))
    clip_make(name,fps,clip_name)
    return 0

if(__name__=="__main__"):
    main()
