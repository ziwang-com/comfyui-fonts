#

#from .zw_def  import *
from .zw_tool  import *
#from .zw_srt  import *
#
#from icecream import ic as cpp
cpp=print
#

#
#from PIL import Image, ImageDraw, ImageFont,ImageColor

#import numpy as np
#
#base_path = os.path.dirname(os.path.realpath(__file__))
base_path=folder_paths.base_path
#cpp(base_path)
# 'D:\\zwai-lab\\ComfyUI'
models_dir=folder_paths.models_dir
#cpp(models_dir)
#'D:\\zwai-lab\\ComfyUI\\models'
#folder_names_and_paths["custom_nodes"]
nodes_dir=folder_paths.folder_names_and_paths["custom_nodes"][0][0]+'/'
temp_dir=folder_paths.temp_directory
#
wrk_dir=f'{nodes_dir}comfyUI-fonts/'
#
#rfsx = os.path.abspath(__file__)
#ZWAI_HOME = os.path.dirname(rfsx)
#cpp(ZWAI_HOME)
#
#ZWAI_HOME = os.environ['ZWAI_HOME']
#fnt_path='/zlib25/font5/'
#cpp(fnt_path)
fnt_path=f'{base_path}/fonts/'
#cpp(fnt_path2)
#
DIC_UTF=f_dictRd(f'{wrk_dir}/assets/gb80_utf.dat')
DIC_XUTF=f_dictRd(f'{wrk_dir}/assets/gb80_xutf.dat')
#
#cpp(folder_paths.folder_names_and_paths)

#
def img_load_fnt(fpath,fsiz):
    #if self._loaded_font is None or use_cache is False:
    #fonts_dir = os.path.join(os.path.dirname(__file__), "fonts")
    #        font_path = os.path.join(fonts_dir, font)
    #if not os.path.exists(font_path):
        #font_path = font

    try:
        xfnt = ImageFont.truetype(fpath, fsiz)
    except Exception as e:
        #print(f"Error loading font: {e}... Using default font")
        #self._loaded_font = ImageFont.load_default(font_size)
        xfnt = ImageFont.load_default(fsiz)
    #
    return xfnt

def img_drtxt(img,txt,fpath,hcor='#00FFFF', fsiz=64,cx=10,cy=10):
    #
    #css=str_fltCR(txt)
    css=txt
    cor=ImageColor.getrgb(hcor)
    xfnt=img_load_fnt(fpath, fsiz)
    draw = ImageDraw.Draw(img)
    #
    draw.text((cx, cy),css,
        #
        fill=cor,
        #fill=self.hex_to_rgb(fill_color_hex),
        #stroke_fill=self.hex_to_rgb(stroke_color_hex),
        #stroke_width=int(font_size * stroke_thickness * 0.5),
        font=xfnt,align='left',)
        #["left", "center", "right"]
    #
    return img


def web_010xget4img(uss):
    #
    #,hdr={"Content-Type": "application/json"}):
    
    #
    #uss=f"https://civitai.com/api/v1/models/{str(xid)}"
    #uss=f"https://civitai.com/api/download/models/{str(xid)}"
    
    #cpp(type(rx))
    img=None
    try:
        cpp(uss)
        rx = requests.get(uss) #, headers=hdr)
        cpp(rx.status_code)
        if rx.status_code == 200:
            ftmp=f'{wrk_dir}tmp/$$$zwfnt$$$.jpg'
            #ftmp='.tmp/$$$zwfnt$$$.jpg'
            with open(ftmp, 'wb') as file:
                file.write(rx.content)
            #
            img=img_rd(ftmp)
            #
            #
            return img
        #mdat = json.loads(rx.text)
        
    except ValueError:
        #print(f"Invalid JSON response for model id: {uss}, URL: {xres.url}")
        #continue
        #pass
        return  None
    #
    return  img
#
#--------------
#
#    
class zw_font_text:
    #
    def __init__(self, device="cpu"):
        self.device = device
    #
    _f100klst=['.ttf','.otf']
    _f100=lst4dir(fnt_path)
    _fntlst=lst_kget8klst(_f100, _f100klst)
    #, kget='', krep='', kflt='', kdir=False):
    #pplst(_fntlst)
    
    

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING",{"multiline": False, "default": "智王大藏经"}),
                "font_size": ("INT", {"default": 128}),
                "x": ("INT", {"default": 100}),
                "y": ("INT", {"default": 100}),
                #"font": ("STRING", {"default": "zwdzj01.ttf"}),  # Assuming it's a path to a .ttf or .otf file
                "font": (cls._fntlst, {"default": "zwdzj01.ttf"}),  # Assuming it's a path to a .ttf or .otf file
                "color": ("STRING", {"default": '#00FFFF'}), #, "min": 0, "max": 0xFFFFFF, "step": 1, "display": "color"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "zw_font_text"
    CATEGORY = "comfyUI-font"
    #CATEGORY = "comfyUI-font"
    #
    #img_drtxt(img,txt,fpath, fsiz=64,cx=10,cy=10):
    def zw_font_text(self, image, text, font_size, x, y, font, color):
        # Convert tensor to numpy array and then to PIL Image
        image_tensor = image
        image_np = image_tensor.cpu().numpy()  # Change from CxHxW to HxWxC for Pillow
        image = Image.fromarray((image_np.squeeze(0) * 255).astype(np.uint8))  # Convert float [0,1] tensor to uint8 image
        #
        #D:\zwai-lab\ComfyUI\fonts\
        #-----------------
        fpath=f'{fnt_path}{font}'
        #cpp(fpath,font)
        #
        img2=img_drtxt(image,text,fpath,hcor=color, fsiz=font_size,cx=x,cy=y)
        #
        #
        #-----------------
        #
        # Convert back to Tensor if needed
        #image_tensor_out = torch.tensor(np.array(image).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.tensor(np.array(img2).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.unsqueeze(image_tensor_out, 0)

        return (image_tensor_out,)

#    
class zw_font_pic:
    def __init__(self, device="cpu"):
        self.device = device
    #
    _rfnt_pic=f'{fnt_path}pic_font/'
    _f100klst=['.jpg','.png','.bmp']
    _fntlst=lst4dir0(_rfnt_pic,kflt=1)
    #
    _vmodlst=['Horizontal','Vertical']
    #_vmod0=
    #_fntlst=lst_kget8klst(_f100, _f100klst)
    #, kget='', krep='', kflt='', kdir=False):
    pplst(_fntlst)
    fnt0='' if len(_fntlst)==0 else _fntlst[0]
        

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING",{"multiline": False, "default": "智王大藏经"}),
                "num_char": ("INT", {"default": 5}),
                "font_size": ("INT", {"default": 128}),
                #
                "x": ("INT", {"default": 100}),
                "y": ("INT", {"default": 100}),
                'wid': ("INT", {"default": 960}),
                'hei': ("INT", {"default": 128}),
                #"font": ("STRING", {"default": "zwdzj01.ttf"}),  # Assuming it's a path to a .ttf or .otf file
                "font": (cls._fntlst, {"default": cls.fnt0}), 
                "fext": (cls._f100klst, {"default": ".png"}), 
                "view_mode": (cls._vmodlst, {"default": "Horizontal"}), 
                 # Assuming it's a path to a .ttf or .otf file
                #"color": ("STRING", {"default": '#00FFFF'}), #, "min": 0, "max": 0xFFFFFF, "step": 1, "display": "color"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "zw_font_pic"
    CATEGORY = "comfyUI-font"
    #
    #img_drtxt(img,txt,fpath, fsiz=64,cx=10,cy=10):
    def zw_font_pic(self, image, text, num_char,font_size, x, y, font, fext,wid,hei,view_mode):
        # Convert tensor to numpy array and then to PIL Image
        image_tensor = image
        image_np = image_tensor.cpu().numpy()  # Change from CxHxW to HxWxC for Pillow
        image = Image.fromarray((image_np.squeeze(0) * 255).astype(np.uint8))  # Convert float [0,1] tensor to uint8 image
        #
        #D:\zwai-lab\ComfyUI\fonts\
        #-----------------
        cpp(fnt_path,font)
        cpp(self._rfnt_pic)
        #_rfnt_pic
        #_rfnt_pic=cls._rfnt_pic
        ulst=str_ucodlst(text,DIC_XUTF)
        flst=[]
        for ucod in ulst:
            fss=f'{self._rfnt_pic}/{font}/{ucod}{fext}'
            flst.append(fss)
            cpp(fss)
        #
        #_vmodlst=['Horizontal','Vertical']
        if view_mode=='Horizontal':
            nrow,ncol=1,num_char
        else:
            nrow,ncol=num_char,1
        #
        img5=imgs_lnk8f(flst, '',nrow, ncol,w=font_size,h=font_size)
        #
        img3 = img5.resize((wid, hei)) #, resample=Image.BILINEAR)
        image.paste(img3, (x,y))
        img2=image
        
        #
        #img2=img_drtxt(image,text,fpath,hcor=color, fsiz=font_size,cx=x,cy=y)
        #img2=image
        #
        #
        #-----------------
        #
        # Convert back to Tensor if needed
        #image_tensor_out = torch.tensor(np.array(image).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.tensor(np.array(img2).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.unsqueeze(image_tensor_out, 0)

        return (image_tensor_out,)


#    
class zw_font_mov:
    #
    def __init__(self, device="cpu"):
        self.device = device
    #
    _f100klst=['.ttf','.otf']
    _f100=lst4dir(fnt_path)
    _fntlst=lst_kget8klst(_f100, _f100klst)
    #, kget='', krep='', kflt='', kdir=False):
    pplst(_fntlst)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING",{"multiline": True, "default": "智王大藏经"}),
                "font_size": ("INT", {"default": 88, "min": 1, "max": 256, "step": 1}),
                "x": ("INT", {"default": 100}),
                "y": ("INT", {"default": 100}),
                #"font": ("STRING", {"default": "zwdzj01.ttf"}),  # Assuming it's a path to a .ttf or .otf file
                "font": (cls._fntlst, {"default": "zwdzj01.ttf"}),  # Assuming it's a path to a .ttf or .otf file
                "color": ("STRING", {"default": '#00FFFF'}), #, "min": 0, "max": 0xFFFFFF, "step": 1, "display": "color"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "zw_font_mov"
    CATEGORY = "comfyUI-font"
    #
    #img_drtxt(img,txt,fpath, fsiz=64,cx=10,cy=10):
    def zw_font_mov(self, image, text, font_size, x, y, font,  color):
        # Convert tensor to numpy array and then to PIL Image
        image_tensor = image
        image_np = image_tensor.cpu().numpy()  # Change from CxHxW to HxWxC for Pillow
        image = Image.fromarray((image_np.squeeze(0) * 255).astype(np.uint8))  # Convert float [0,1] tensor to uint8 image
        #
        #D:\zwai-lab\ComfyUI\fonts\
        #-----------------
        fpath=f'{fnt_path}{font}'
        cpp(fpath,font)
        
        #
        img2=img_drtxt(image,text,fpath,hcor=color, fsiz=font_size,cx=x,cy=y)
        #
        #
        #-----------------
        #
        # Convert back to Tensor if needed
        #image_tensor_out = torch.tensor(np.array(image).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.tensor(np.array(img2).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.unsqueeze(image_tensor_out, 0)

        return (image_tensor_out,)


#    
class zw_font_api:
    #
    def __init__(self, device="cpu"):
        self.device = device
    #
    #_f100klst=['.ttf','.otf']
    #_f100=lst4dir(fnt_path)
    #_fntlst=lst_kget8klst(_f100, _f100klst)
    #, kget='', krep='', kflt='', kdir=False):
    #pplst(_fntlst)
    us0='http://frp.snakelenas.top:2101/api/'
    us2='http://m-f.vip/api/'
    us3='http://ziwang.com/api/'
    _urllst=[us0,us2,us3]
    #
    ftyp0='truetype'
    ftyp2='png'
    ftyp3='gif'
    _fntyplst=[ftyp0,ftyp2,ftyp3]
    #
    fnt0='zw.FAT4_003J.ttf'   #zwdzj01.ttf"
    

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING",{"multiline": True, "default": "智王大藏经"}),
                "font_size": ("INT", {"default": 128, "min": 1, "max": 256, "step": 1}),
                "x": ("INT", {"default": 100}),
                "y": ("INT", {"default": 100}),
                'wid': ("INT", {"default": 960}),
                'hei': ("INT", {"default": 128}),
                #"font": ("STRING", {"default": "zwdzj01.ttf"}),  # Assuming it's a path to a .ttf or .otf file
                "font_type": (cls._fntyplst, {"default": cls.ftyp0}),  # Assuming it's a path to a .ttf or .otf file
                #"font": (cls._fntlst, {"default": "zwdzj01.ttf"}),  # Assuming it's a path to a .ttf or .otf file
                "font": ('STRING', {"default": cls.fnt0}),  # Assuming it's a path to a .ttf or .otf file
                "api_url": (cls._urllst, {"default": cls.us0}),  # Assuming it's a path to a .ttf or .otf file
                #"color": ("STRING", {"default": '#00FFFF'}), #, "min": 0, "max": 0xFFFFFF, "step": 1, "display": "color"}),
                
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "zw_font_api"
    CATEGORY = "comfyUI-font"
    #
    #img_drtxt(img,txt,fpath, fsiz=64,cx=10,cy=10):
    def zw_font_api(self, image, text, font_size,x, y, font,api_url, font_type,wid,hei):
        # Convert tensor to numpy array and then to PIL Image
        image_tensor = image
        image_np = image_tensor.cpu().numpy()  # Change from CxHxW to HxWxC for Pillow
        image = Image.fromarray((image_np.squeeze(0) * 255).astype(np.uint8))  # Convert float [0,1] tensor to uint8 image
        #
        #D:\zwai-lab\ComfyUI\fonts\
        #-----------------
        fpath=f'{fnt_path}{font}'
        #cpp(fpath,font,fnt_path)
        #http://frp.snakelenas.top:2101/api/truetype?f=zw.FAT4_003J.ttf&t=我的AI操作面板&s=56
        #
        uss=f'{api_url}{font_type}?f={font}&s={font_size}&t={text}'
        img5=web_010xget4img(uss)
        #ftmp=f'{wrk_dir}tmp/$$$zwfnt$$$02.jpg'
        #img2=img_rd(ftmp)
        img3 = img5.resize((wid, hei)) #, resample=Image.BILINEAR)
        image.paste(img3, (x,y))
        #cpp(ftmpx)
        #
        img2=image
        
        #img2=img_drtxt(image,text,fpath,hcor=color, fsiz=font_size,cx=x,cy=y)
        #
        #
        #-----------------
        #
        # Convert back to Tensor if needed
        #image_tensor_out = torch.tensor(np.array(image).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.tensor(np.array(img2).astype(np.float32) / 255.0)  # Convert back to CxHxW
        image_tensor_out = torch.unsqueeze(image_tensor_out, 0)

        return (image_tensor_out,)

    


class zw_ucod:
    def __init__(self, device="cpu"):
        self.device = device
    #
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING",{"multiline": False, "default": "智王大藏经"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "zw_ucod_debug"
    CATEGORY = "comfyUI-font/debug"
    #
    #img_drtxt(img,txt,fpath, fsiz=64,cx=10,cy=10):
    def zw_ucod_debug(self, text):
        # Convert tensor to numpy array and then to PIL Image
        #
        cpp(text)
        ulst=str_ucodlst(text,DIC_XUTF)
        tss=','.join(ulst)
        cpp(tss)
        cpp(ulst)
        
        #

        return (tss,)

        
        
NODE_CLASS_MAPPINGS = {
    #
    "zw-font": zw_font_text,
    #
    "zw-font-api": zw_font_api,
    #
    "zw-font-pic": zw_font_pic,
    #"zw-font-mov": zw_font_mov,
    #
    "zw-font-ucode": zw_ucod,
}
