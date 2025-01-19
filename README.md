# comfyUI-fonts
 
![cfnt001](https://github.com/user-attachments/assets/6fa46a33-68a1-4360-bb0e-8b132d0b3c6a)

* comfy-font万能字体节点node，支持truetype，freetype，open1等经典字库格式，也支持jpg、png等图片格式，还支持gif、短视频等各种视频格式，以及api接口。
* Comfy font universal font node, supporting classic font library formats such as Truetype, FreeType, Open1, as well as image formats such as JPG and PNG. It also supports various video formats such as GIF and short videos, as well as API interfaces.

# 安装
ComfyUI-fonts
## 使用 ComfyUI Manager：
在 ComfyUI 管理器中，查找ComfyUI-fonts.安装它。

## 手动安装#1：
* 将此仓库克隆到 ComfyUI 中的文件夹custom_nodes中并安装依赖项。
* cd custom_nodes
* git clone https://github.com/ziwang-com/comfyui_fonts.git

## 手动安装#2：
* 在https://github.com/ziwang-com/comfyui_fonts下载项目打包文件。
* 解压，把解压后的目录改为：comfyui_fonts
* 手动copy到custom_nodes目录

### 正确目录结构为：
* ComfyUI/custom_nodes/comfyui_fonts
* 

## 主要节点
* zw-font: 本地标准ttf字体文件接口
* zw-font-pic: 本地图像字体文件接口
*  #
* zw-font-api: 远程服务器api接口，云字库模式
* zw-font-ucode: 内置字符串-ucod转换节点
* zw-font-mov: 隐含节点，未开放，动态视频字体接口
  
###  assets资源目录
* 有demo-workflow工作流
* 配套的图像素材
* 两套开源中文字体：字王大藏经开源字体，阿里普惠体
* 默认ttf字体文件，须copy复制到以下目录：
* ComfyUI/fonts
  
  ![zwfnt-dir](https://github.com/user-attachments/assets/1a24c4be-0236-45f3-9705-84264f594b09)

![zwfnt-dir-pic-ucod](https://github.com/user-attachments/assets/3d78fb97-6818-4ef4-9343-feff7b5d45bd)

![zwfnt-dir-mov-ucod](https://github.com/user-attachments/assets/0829cbda-d186-42b3-ba6b-fb4331ccfd7f)



## 主要节点-demo
# 参见assets资源目录，有demo-workflow工作流
![cfnt001](https://github.com/user-attachments/assets/8bdc7efe-8817-4195-82bc-ce3d424f8480)

![cfnt002pic-v](https://github.com/user-attachments/assets/10f74249-7df8-44d3-82ed-73a426a62603)

![cfnt011ucod](https://github.com/user-attachments/assets/33c41225-2c1f-4bfd-be4d-e9d7aefe6c78)

![cfnt011ucod2](https://github.com/user-attachments/assets/27c93537-6c9a-482d-915f-bb3c155a4f84)


## 补充说明
*  字体使用，有严格的IP版权规定，请大家注意相关法规。
*  除ttf字体文件接口外，其他节点尚未加入去底功能。
*  api远程模式，调用的是内部测试服务器。
*  未来会增加字幕、动态切换、数字人、短视频集成等功能。
*  #
*  zwai团队，超过30年AI字王字体开放经验。
*  独家拥有1w套以上字王字库IP版权，国标二级。
*  授权方式灵活，有兴趣的结构和个人，请联系zwai开源组负责人。

  ![image](https://github.com/user-attachments/assets/652e3660-1ff6-47d1-b815-ae26c650c2b6)




