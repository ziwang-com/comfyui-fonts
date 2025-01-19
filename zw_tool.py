# -*- coding: utf-8 -*- 
#


#-----------------

#from .zw_def import *

import os,torch
import requests
#
import numpy as np
from pathlib import Path
from PIL import Image, PngImagePlugin, ImageDraw, ImageFont, ImageColor, ImageChops, ImageOps, ImageFilter
from PIL.Image import fromarray
#

import folder_paths
#
# -----------init.xxx
#
cpp=print
#
def pplst(dlst,n=3):
    #

    if (len(dlst) > 0) and dlst is not None:
        cpp(len(dlst), dlst[:n])


#---
#
def str_ucodlst(clst,xdic,n0=4):
    #cs2=str_ucodlst(us2,xdic_utf)
    u10=[]
    for c in clst:
        #ucod=str_hex(c).upper()
        ucod=xdic.get(c,'')
        u10.append(ucod)
    #
    return u10


def f_is(fnam, kpr=0):
    '''
    文件，路径，存在判定函数
    输入；
        fnam，文件，路径名称，路径可以是相对目录
    输出：
        xfg，判定结果

    '''
    # xx
    fnam = str(fnam)
    fnam = fnam.lstrip().rstrip()
    xfg = False
    if fnam != '':
        my_file = Path(fnam)
        # xfg= (my_file.is_file())or(my_file.is_dir())
        xfg = my_file.exists()
    #
    if kpr:
        cpp(xfg, fnam)

    return xfg


def f_rd(fn,cod='utf8'):
    #
    if not f_is(fn):return ''
    #
    f=open(fn,'r',encoding=cod)
    dss=f.read()
    f.close()
    return dss

def f_dictRd(fn, cod='utf8'):
    xdat = f_rd(fn, cod=cod)
    return eval(xdat)

def lst_xrep(dlst, kstr0, newstr):
    xlst, kstr = [], kstr0.lower()
    # pp(['@kstr',kstr])
    for xd in dlst:
        xd = str(xd)
        dss = xd.lower()
        tss = dss.replace(kstr, newstr)
        xlst.append(tss)
        # pp(['@x',xlst])
    #
    return xlst

def lst_kget(dlst, kstr0):
    xlst, kstr = [], kstr0.lower()
    # cpp(kstr)
    for xd in dlst:
        xd = str(xd)
        dss = xd.lower()
        xc = dss.find(kstr)
        # cpp(xc,dss)
        if xc > -1:
            xlst.append(xd)
            # cpp(xd,xlst)
            # xxx
    #
    xlst = list(set(xlst))
    #
    return xlst


def lst_kget8klst(dlst, klst):
    tlst = []
    for kss in klst:
        d10 = lst_kget(dlst, kss)
        tlst = tlst + d10
    #
    tlst = list(set(tlst))
    #
    return tlst


def lst4dir0(rsx,kflt=0):
    ''' 子目录生成列表数据
    in：
        rsx，目录名称
    out：
        mlst；rss目录下的子目录，列表格式, 不包含路径

        xxx

    '''
    rsx = str(rsx)
    p = Path(rsx + '.')
    mlst = [str(x) for x in p.iterdir() if x.is_dir()]
    #cpp(rsx,p,mlst)
    #
    if kflt:
        rs2 = rsx.replace('/', '\\')
        mlst=lst_xrep(mlst,rs2,'')
        #mlst = lst_xrep(mlst, rsx, '')
    #

    # xx
    return mlst


def lst4dir(rss, kget='', krep='', kflt='', kdir=False):
    '''
    # flst = get_image_files(rtst)
    from fastai.vision.all import *
    目录文件生成列表数据
    in：
        rss，目录名称，可以是相对目录,rss='topqt2/'
    out：
        flst；rss目录下的文件名，列表格式, 包含路径
    #
    #rdat=Path(rdat)
    #flst = [f for f in rdat.rglob("*.*")]
    #
    '''
    # rlst=os.listdir(rs0)    ::['data', 'files', 'model']

    flst = []
    krep, kget, kflt = krep.lower(), kget.lower(), kflt.lower()
    for root, dirs, files in os.walk(rss):
        for fss in files:
            fss = fss.lower()
            fss=fss.replace('\\','/')
            # cpp(fss)
            # print(fss)
            # ppp([root,dirs,fss])
            #
            if kget != '':
                if fss.find(kget) < 0:
                    fss = ''
            #
            if krep != '':
                fss = fss.replace(krep, '')
            #

            if kflt != '':
                if fss.find(kflt) < -1:
                    fss = ''
            #
            if fss != '':
                if kdir:
                    fss = root + '/' + fss

                flst.append(fss)

    #
    return flst


def img_rd(path,cov='RGB'):
    path=str(path)
    #ppp(path)
    with open(path, "rb") as f, Image.open(f) as img:
        if cov!='':
            img=img.convert("RGB")
        return img


def imgs_lnk8f(flst, ftg,nrow=1, ncol=1,w=1024,h=1024):
    #
    to_image = Image.new('RGB', (ncol * w, nrow * h))  
    from_image = None
    xn=len(flst)
    for y in range(1, nrow + 1):
        for x in range(1, ncol + 1):
            fss=flst[ncol * (y - 1) + x - 1]
            xfg=f_is(fss,1)
            if (ncol * (y - 1) + x - 1 > xn - 1) or (not xfg):
                from_image = Image.new('RGB', (w,h), (255, 255, 255))
            else:
                from_image = Image.open(fss).resize((w,h)) 
            #
            to_image.paste(from_image, ((x - 1) * w, (y - 1) * h))
    #
    if ftg!='':
        f_gifWr(ftg, [to_image], tn=100)
    #
    return to_image