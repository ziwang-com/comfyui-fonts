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

## 主要节点
* zw-font: 本地标准字体文件接口
* zw-font-pic: 本地图像字体文件接口
*  #
* zw-font-api: 远程服务器api接口，云字库模式
* zw-font-ucode: 内置字符串-ucod转换节点
* zw-font-mov: 隐含节点，未开放，动态视频字体接口
*   zw_font_api,
    #
    "zw-font-pic": zw_font_pic,
    #"zw-font-mov": zw_font_mov,
    #
    "zw-font-ucode": zw_ucod,
