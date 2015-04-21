# coding=utf-8
'''
Created on 22 апр. 2015 г.

@author: Ziobr
'''
from distutils.core import setup
import py2exe
import sys
import os
import os.path
sys.argv.append ('py2exe')
sys.path.append('src')
setup (
       data_files = [('../data', ["src/data/code.txt"])],
       options    = 
            {'py2exe': 
                { "bundle_files" : 2    # 3 = don't bundle (default) 
                                         # 2 = bundle everything but the Python interpreter 
                                         # 1 = bundle everything, including the Python interpreter
                , "compressed"   : False  # (boolean) create a compressed zipfile
                , "unbuffered"   : False  # if true, use unbuffered binary stdout and stderr
                , "includes"     : 
                    [ "tkinter", "tkinter.ttk", "CryptoLabs"
    
                    ]
                , "excludes"      : ["tcl", ]
                , "optimize"     : 0  #-O
                , "packages"     : 
                    [ 
                    ]
                , "dist_dir"     : "build"
                , "dll_excludes": ["tcl85.dll", "tk85.dll"]
                ,              
                }
            }
        , windows    = 
            ["src/GUI/MainWindow.py"]
        , zipfile    = None
        # the syntax for data files is a list of tuples with (dest_dir, [sourcefiles])
        # if only [sourcefiles] then they are copied to dist_dir 
        #, data_files = [   os.path.join (sys.prefix, "DLLs", f) 
        #               for f in os.listdir (os.path.join (sys.prefix, "DLLs")) 
        #               if  (   f.lower ().startswith (("tcl", "tk")) 
        #                   and f.lower ().endswith ((".dll", ))
        #                   )
        #                ] 
    
        , 
)