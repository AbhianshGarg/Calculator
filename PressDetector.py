def Detector(x, y, startx, starty, height, width, spaceheight, spacewidth, row_one, row_two, row_three, row_four, row_five):
    if starty < x < starty + height:
        if startx - width*0 < y < startx - width*1:
            press =  1
        elif startx - width*1 < y < startx - width*2:
            press = 1
        elif startx - width*2 < y < startx - width*3:
            press = 1

