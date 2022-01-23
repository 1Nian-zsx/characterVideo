import tkinter
import tkinter.filedialog
import cv2
from PIL import Image, ImageDraw, ImageFont
from matplotlib.pyplot import grid
import numpy as np
import threading

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!1I;:,\"^ `'.")
root=tkinter.Tk()
root.title('视频转字符画')
root.geometry('450x110')
inputPath=tkinter.StringVar()
outputPath=tkinter.StringVar()
totalFrames=tkinter.IntVar()
num=tkinter.IntVar()
totalFrames.set(0)
num.set(0)

def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()

def charVideo(input,output):
    vc = cv2.VideoCapture(input.get())
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    outputname=output.get()+"/output.avi"
    fps=int(vc.get(cv2.CAP_PROP_FPS))
    videoWriter = cv2.VideoWriter(outputname, fourcc, fps, (1920, 1080))
    Num=0
    totalFrames.set(int(vc.get(cv2.CAP_PROP_FRAME_COUNT)))
    ret = vc.isOpened()
    while ret:
        ret, frame = vc.read()
        if ret:
            Num+=1
            num.set(Num)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            img_array = np.array(cv2.resize(gray,(240, 135)))
            img = Image.new('L', (1920, 1080), 255)
            draw_object = ImageDraw.Draw(img)
            font = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 10, encoding='unic')
            for j in range(135):
                for k in range(240):
                    x, y = k * 8, j * 8
                    index = img_array[j][k] // 4
                    draw_object.text((x, y), ascii_char[index], font=font, fill=0)
            charimg=cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
            videoWriter.write(charimg)
        else:
            break
    vc.release()
    videoWriter.release()
    button['state'] = tkinter.NORMAL
    tkinter.messagebox.showinfo('提示','转换完成')

def selectInputPath():
    path_ = tkinter.filedialog.askopenfilename()
    inputPath.set(path_)

def selectOutputPath():
    path_ = tkinter.filedialog.askdirectory()
    outputPath.set(path_)

def start():
    button['state'] = tkinter.DISABLED
    charVideo(inputPath,outputPath)

tkinter.Label(root,text="输入文件:").grid(row=0,column=0)
tkinter.Entry(root,textvariable=inputPath).grid(row=0,column=1)
tkinter.Button(root,text="选择",command=selectInputPath).grid(row=0,column=2)

tkinter.Label(root,text="输出路径:").grid(row=1,column=0)
tkinter.Entry(root,textvariable=outputPath).grid(row=1,column=1)
tkinter.Button(root,text="选择",command=selectOutputPath).grid(row=1,column=2)

button=tkinter.Button(root,text="开始",command=lambda :thread_it(start))
button.grid(row=2,column=1)

tkinter.Label(root,text="正在转换第").grid(row=3,column=2)
tkinter.Label(root,textvariable=num).grid(row=3,column=3)
tkinter.Label(root,text="帧，共").grid(row=3,column=4)
tkinter.Label(root,textvariable=totalFrames).grid(row=3,column=5)
tkinter.Label(root,text="帧").grid(row=3,column=6)

root.mainloop()

