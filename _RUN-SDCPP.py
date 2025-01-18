import subprocess
import random
import string
from datetime import datetime
from PIL import Image
from PIL.PngImagePlugin import PngInfo
# for pillow
# https://medium.com/generative-ai/generate-images-cpp-is-this-a-thing-d7f5f11a0e0e
# https://stackoverflow.com/questions/58399070/how-do-i-save-custom-information-to-a-png-image-file-in-python
# maybe a gradio log https://github.com/louis-she/gradio-log
# aspect ratio calculator https://calculateaspectratio.com/
# subprocess https://python.land/operating-system/python-subprocess
# https://www.geeksforgeeks.org/executing-shell-commands-with-python/
# https://docs.python.org/3/library/subprocess.html#module-subprocess
# MODEL https://huggingface.co/Lykon/DreamShaper  > dreamshaper_8.safetensors


def genRANstring(n):
    """
    n = int number of char to randomize
    Return -> str, the filename with n random alphanumeric charachters
    """
    N = n
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    print(f'Logfile_{res}.png  CREATED')
    return f'IMAGE_SDCPP_{res}.png'

fILENAME = genRANstring(5)
PROMPT = input('/IMAGINE ')
STEPS = input('Number of Steps: ')
WIDTH = '512'
HEIGHT = '256'
print(f'Saving the Generated image with dreamshaper_8 as: {fILENAME}')
start = datetime.now()
mc = ['sd.exe',
    '-m',
    'dreamshaper_8.safetensors',
    '--cfg-scale',
    '5',
    '--steps',
    STEPS,
    '-W',
    WIDTH,
    '-H',
    HEIGHT,
    '--sampling-method',
    'euler',
    '-p',
    PROMPT,
    '-o',
    fILENAME]
res = subprocess.call(mc,shell=True)
delta = datetime.now() - start
print(f'Completed in {delta}')
metadata = PngInfo()
metadata.add_text("Prompt", PROMPT)
metadata.add_text("ImageSize", f'WxH: {WIDTH} x {HEIGHT}')
metadata.add_text("Steps", f'Steps: {STEPS} Sampling Method: euler')
metadata.add_text("GenerationTime", f'{str(delta)}')
targetimage = Image.open(fILENAME)
targetimage.save(fILENAME,pnginfo=metadata)
print(f'Saved all images METADATA in {fILENAME}')
print(targetimage.text)
targetimage.show()





