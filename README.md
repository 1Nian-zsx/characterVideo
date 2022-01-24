# 将普通视频转换为字符画视频，目前输出为1080p  
需要用到的库有cv2（pip install opencv-python），PIL（pip install pillow），matplotlib（pip install matplotlib），numpy（pip install numpy）  
两个文件没太大区别，做两版只是因为windows和macOS字体不同而已，并且两个系统UI比例也不一样，不是什么大问题  
v1.1 现在可以不逐帧输出再合并成视频了  
v1.2 添加了UI界面，可以选择输入文件和输出路径，不需要将视频放在同级文件夹下  
v1.3 更新了UI界面，添加了转换进度显示  
v1.4 更新了视频转换选项，现在会自动检测输入视频的帧率作为输出视频的帧率  
v1.5 更新了UI界面，现在转换完成前不能点击开始按钮开始新的转换  
计划中的更新：  
1、导出时可选分辨率和帧率  
2、导出时可更改文件名（现为固定output.avi）  
3、导出视频文件过大的问题  
4、美化UI  
5、提升转换效率
