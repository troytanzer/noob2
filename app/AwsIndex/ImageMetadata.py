import glob

def generate_album_index(album_name, newpicsdir):
    index_info = []
    glob_string = os.path.join('.', '*.jpg')
    files = glob.glob(glob_string)
    for f in [os.path.basename(x) for x in files]:
        d = dict()
        d['thumb'] = f'thumbs/{f}'
        d['medium'] = f'medium/{f}'
        d['large'] = f'large/{f}'
        d['title'] = f'{album_name} - {f}'
        d['createDate'] = 0
        d['description'] = ''
        d['location'] = {}
        d['imageSize'] = {'height' : 500, 'width' : 500}
        d['isCover'] = False
        d['filename'] = f'{f}'
        d['src'] = f'{newpicsdir}/{f}'
        # TODO if it is a file, this is an image, if it is a directory then it is a gallery.  Theoretically, we could have a gallery containing both
        # other galleries and images, so we should support that, but right now it doesn't.  The HTML will be slightly different for images and galleries
        d['type'] = 'image'
        #print(d)
        index_info.append(d)
    return index_info

def generate_album_html(album_name, newpicsdir):
    #Tons of boilerplate at beginning
    glob_string = os.path.join(newpicsdir, '*.jpg')
    files = glob.glob(glob_string)
    logger.debug(files)
    for file_name in [os.path.basename(x) for x in files]:
        #switch to dictionary
        pic_html = HTML_IMAGE.substitute(file_name=file_name, album_name=album_name)
        print(pic_html)
