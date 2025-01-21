# StableDiffusionCPP-usage
Create images with dreamshaper_8 on your CPU
<img src='https://github.com/fabiomatricardi/StableDiffusionCPP-usage/raw/main/20250118-firstIMAGE1344x768.png' width=900>

Image generated with dreamshaper_8 and sd.cpp
```
 .\sd.exe -m .\dreamshaper_8.safetensors --cfg-scale 5 --steps 10 --sampling-method euler -H 768 -W 1344 -p "fantasy medieval village world inside a glass sphere , high detail, fantasy, realistic, light effect, hyper detail, volumetric lighting, cinematic, macro, depth of field, blur, red light and clouds from the back, highly detailed epic cinematic concept art cg render made in maya, blender and photoshop, octane render, excellent composition, dynamic dramatic cinematic lighting, aesthetic, very inspirational, world inside a glass sphere by james gurney by artgerm with james jean, joe fenton and tristan eaton by ross tran, fine details, 4k resolution"
```
### generated in 85 minutes!!!

Extract of the LOG
```
[INFO ] stable-diffusion.cpp:195  - loading model from '.\dreamshaper_8.safetensors'
[INFO ] model.cpp:888  - load .\dreamshaper_8.safetensors using safetensors format
[INFO ] stable-diffusion.cpp:242  - Version: SD 1.x
[INFO ] stable-diffusion.cpp:275  - Weight type:                 f16
[INFO ] stable-diffusion.cpp:276  - Conditioner weight type:     f16
[INFO ] stable-diffusion.cpp:277  - Diffusion model weight type: f16
[INFO ] stable-diffusion.cpp:278  - VAE weight type:             f16
  |==================================================| 1130/1130 - 125.00it/s
[INFO ] stable-diffusion.cpp:516  - total params memory size = 1969.78MB (VRAM 0.00MB, RAM 1969.78MB): clip 235.06MB(RAM), unet 1640.25MB(RAM), vae 94.47MB(RAM), controlnet 0.00MB(VRAM), pmid 0.00MB(RAM)
[INFO ] stable-diffusion.cpp:520  - loading model from '.\dreamshaper_8.safetensors' completed, taking 4.97s
[INFO ] stable-diffusion.cpp:550  - running in eps-prediction mode
[INFO ] stable-diffusion.cpp:682  - Attempting to apply 0 LoRAs
[INFO ] stable-diffusion.cpp:1235 - apply_loras completed, taking 0.00s
[INFO ] stable-diffusion.cpp:1368 - get_learned_condition completed, taking 1572 ms
[INFO ] stable-diffusion.cpp:1391 - sampling using Euler method
[INFO ] stable-diffusion.cpp:1428 - generating image: 1/1 - seed 42
  |==================================================| 10/10 - 477.33s/it
[INFO ] stable-diffusion.cpp:1466 - sampling completed, taking 4613.73s
[INFO ] stable-diffusion.cpp:1474 - generating 1 latent images completed, taking 4613.85s
[INFO ] stable-diffusion.cpp:1477 - decoding 1 latents
[INFO ] stable-diffusion.cpp:1487 - latent 1 decoded, taking 490.42s
[INFO ] stable-diffusion.cpp:1491 - decode_first_stage completed, taking 490.43s
[INFO ] stable-diffusion.cpp:1614 - txt2img completed in 5105.87s
save result image to 'output.png'  now renamed as 20250118-firstIMAGE1344x768.png
```

### Stable Diffusion CPP
A pure CPP implementation of the [diffusion transformers library inspired by llama.cpp](https://github.com/leejet/stable-diffusion.cpp)
- GitHub repo [here](https://github.com/leejet/stable-diffusion.cpp)
- Per Compiled libraries [here](https://github.com/leejet/stable-diffusion.cpp/releases)
> note that if you have a GPU you must download the Vulkan or the CUDA binaries

It allows you to run diffusion models even on CPU, using also quantized versions of the models.
- model can be downloaded [here](https://huggingface.co/Lykon/DreamShaper)
- guide to use `subprocess` library is [here](https://python.land/operating-system/python-subprocess)
- inspired from my previous article, but easier [https://medium.com/generative-ai/generate-images-cpp-is-this-a-thing-d7f5f11a0e0e](https://medium.com/generative-ai/generate-images-cpp-is-this-a-thing-d7f5f11a0e0e)
- for how to [add metadata to PNG files](https://stackoverflow.com/questions/58399070/how-do-i-save-custom-information-to-a-png-image-file-in-python)

```python
import subprocess
import random
import string
from datetime import datetime
from PIL import Image
from PIL.PngImagePlugin import PngInfo

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
```

### TEST 2
```
TEST2
./sd.exe -m ./dreamshaper_8.safetensors --cfg-scale 5 --steps 10 --sampling-method euler -W 512 -H 256 -p 'fantasy stone-age village world high detail, fantasy, realistic, light effect, hyper detail, volumetric lighting, cinematic, macro, depth of field, blur, red light and clouds from the back, anime style' -o 20250118-test_1steps.png
[INFO ] stable-diffusion.cpp:195  - loading model from './dreamshaper_8.safetensors'
[INFO ] model.cpp:888  - load ./dreamshaper_8.safetensors using safetensors format
[INFO ] stable-diffusion.cpp:242  - Version: SD 1.x
[INFO ] stable-diffusion.cpp:275  - Weight type:                 f16
[INFO ] stable-diffusion.cpp:276  - Conditioner weight type:     f16
[INFO ] stable-diffusion.cpp:277  - Diffusion model weight type: f16
[INFO ] stable-diffusion.cpp:278  - VAE weight type:             f16
  |==================================================| 1130/1130 - 250.00it/s
[INFO ] stable-diffusion.cpp:516  - total params memory size = 1969.78MB (VRAM 0.00MB, RAM 1969.78MB): clip 235.06MB(RAM), unet 1640.25MB(RAM), vae 94.47MB(RAM), controlnet 0.00MB(VRAM), pmid 0.00MB(RAM)
[INFO ] stable-diffusion.cpp:520  - loading model from './dreamshaper_8.safetensors' completed, taking 2.98s
[INFO ] stable-diffusion.cpp:550  - running in eps-prediction mode
[INFO ] stable-diffusion.cpp:682  - Attempting to apply 0 LoRAs
[INFO ] stable-diffusion.cpp:1235 - apply_loras completed, taking 0.00s
[INFO ] stable-diffusion.cpp:1368 - get_learned_condition completed, taking 2057 ms
[INFO ] stable-diffusion.cpp:1391 - sampling using Euler method
[INFO ] stable-diffusion.cpp:1428 - generating image: 1/1 - seed 42
  |==================================================| 10/10 - 31.26s/it
[INFO ] stable-diffusion.cpp:1466 - sampling completed, taking 316.97s
[INFO ] stable-diffusion.cpp:1474 - generating 1 latent images completed, taking 317.10s
[INFO ] stable-diffusion.cpp:1477 - decoding 1 latents
[INFO ] stable-diffusion.cpp:1487 - latent 1 decoded, taking 64.99s
[INFO ] stable-diffusion.cpp:1491 - decode_first_stage completed, taking 64.99s
[INFO ] stable-diffusion.cpp:1614 - txt2img completed in 384.15s
save result image to '20250118-IMAGE512x256_stoneage_10steps.png'

```

### TEST 3
```
python .\_RUN-SDCPP.py
Logfile_4NWJO.png  CREATED
/IMAGINE sci-fi village world inside a glass sphere , high detail, fantasy, realistic, light effect, hyper detail, volumetric lighting, cinematic, macro, depth of field, blur, red light and clouds from the back, highly detailed epic cinematic concept art cg render made in maya, blender and photoshop, octane render, excellent composition, dynamic dramatic cinematic lighting, aesthetic, very inspirational, world inside a glass sphere by james gurney by artgerm with james jean, joe fenton and tristan eaton by ross tran, fine details, 4k resolution
Number of Steps: 10
Saving the Generated image with dreamshaper_8 as: IMAGE_SDCPP_4NWJO.png
[INFO ] stable-diffusion.cpp:195  - loading model from 'dreamshaper_8.safetensors'
[INFO ] model.cpp:888  - load dreamshaper_8.safetensors using safetensors format
[INFO ] stable-diffusion.cpp:242  - Version: SD 1.x
[INFO ] stable-diffusion.cpp:275  - Weight type:                 f16
[INFO ] stable-diffusion.cpp:276  - Conditioner weight type:     f16
[INFO ] stable-diffusion.cpp:277  - Diffusion model weight type: f16
[INFO ] stable-diffusion.cpp:278  - VAE weight type:             f16
  |==================================================| 1130/1130 - 200.00it/s
[INFO ] stable-diffusion.cpp:516  - total params memory size = 1969.78MB (VRAM 0.00MB, RAM 1969.78MB): clip 235.06MB(RAM), unet 1640.25MB(RAM), vae 94.47MB(RAM), controlnet 0.00MB(VRAM), pmid 0.00MB(RAM)
[INFO ] stable-diffusion.cpp:520  - loading model from 'dreamshaper_8.safetensors' completed, taking 2.80s
[INFO ] stable-diffusion.cpp:550  - running in eps-prediction mode
[INFO ] stable-diffusion.cpp:682  - Attempting to apply 0 LoRAs
[INFO ] stable-diffusion.cpp:1235 - apply_loras completed, taking 0.00s
[INFO ] stable-diffusion.cpp:1368 - get_learned_condition completed, taking 1984 ms
[INFO ] stable-diffusion.cpp:1391 - sampling using Euler method
[INFO ] stable-diffusion.cpp:1428 - generating image: 1/1 - seed 42
  |==================================================| 10/10 - 31.41s/it
[INFO ] stable-diffusion.cpp:1466 - sampling completed, taking 312.87s
[INFO ] stable-diffusion.cpp:1474 - generating 1 latent images completed, taking 313.01s
[INFO ] stable-diffusion.cpp:1477 - decoding 1 latents
[INFO ] stable-diffusion.cpp:1487 - latent 1 decoded, taking 64.68s
[INFO ] stable-diffusion.cpp:1491 - decode_first_stage completed, taking 64.68s
[INFO ] stable-diffusion.cpp:1614 - txt2img completed in 379.68s
save result image to 'IMAGE_SDCPP_4NWJO.png'
Completed in 0:06:22.814748

```

### TEST 4
```
Test with CivitaAI prompt
a fantasy city built within a vast cave, sleek glass buildings, elegant walkways between towers, illustration, raining, dark and moody lighting, digital art, oil painting, fantasy, 8 k, trending on artstation, detailed
OrIGINaL IMAGE 52265249.jpeg

> python .\_RUN-SDCPP.py
Logfile_GMGSB.png  CREATED
/IMAGINE a fantasy city built within a vast cave, sleek glass buildings, elegant walkways between towers, illustration, raining, dark and moody lighting, digital art, oil painting, fantasy, 8 k, trending on artstation, detailed
Number of Steps: 10
Saving the Generated image with dreamshaper_8 as: IMAGE_SDCPP_GMGSB.png
[INFO ] stable-diffusion.cpp:195  - loading model from 'dreamshaper_8.safetensors'
[INFO ] model.cpp:888  - load dreamshaper_8.safetensors using safetensors format
[INFO ] stable-diffusion.cpp:242  - Version: SD 1.x
[INFO ] stable-diffusion.cpp:275  - Weight type:                 f16
[INFO ] stable-diffusion.cpp:276  - Conditioner weight type:     f16
[INFO ] stable-diffusion.cpp:277  - Diffusion model weight type: f16
[INFO ] stable-diffusion.cpp:278  - VAE weight type:             f16
  |==================================================| 1130/1130 - 200.00it/s
[INFO ] stable-diffusion.cpp:516  - total params memory size = 1969.78MB (VRAM 0.00MB, RAM 1969.78MB): clip 235.06MB(RAM), unet 1640.25MB(RAM), vae 94.47MB(RAM), controlnet 0.00MB(VRAM), pmid 0.00MB(RAM)
[INFO ] stable-diffusion.cpp:520  - loading model from 'dreamshaper_8.safetensors' completed, taking 3.25s
[INFO ] stable-diffusion.cpp:550  - running in eps-prediction mode
[INFO ] stable-diffusion.cpp:682  - Attempting to apply 0 LoRAs
[INFO ] stable-diffusion.cpp:1235 - apply_loras completed, taking 0.00s
[INFO ] stable-diffusion.cpp:1368 - get_learned_condition completed, taking 1229 ms
[INFO ] stable-diffusion.cpp:1391 - sampling using Euler method
[INFO ] stable-diffusion.cpp:1428 - generating image: 1/1 - seed 42
  |==================================================| 10/10 - 30.67s/it
[INFO ] stable-diffusion.cpp:1466 - sampling completed, taking 324.79s
[INFO ] stable-diffusion.cpp:1474 - generating 1 latent images completed, taking 324.98s
[INFO ] stable-diffusion.cpp:1477 - decoding 1 latents
[INFO ] stable-diffusion.cpp:1487 - latent 1 decoded, taking 64.80s
[INFO ] stable-diffusion.cpp:1491 - decode_first_stage completed, taking 64.80s
[INFO ] stable-diffusion.cpp:1614 - txt2img completed in 391.02s
save result image to 'IMAGE_SDCPP_GMGSB.png'
Completed in 0:06:34.646274
Saved all images METADATA in IMAGE_SDCPP_GMGSB.png
{'parameters': 'a fantasy city built within a vast cave, sleek glass buildings, elegant walkways between towers, illustration, raining, dark and moody lighting, digital art, oil painting, fantasy, 8 k, trending on artstation, detailed\nSteps: 10, CFG scale: 5.000000, Guidance: 3.500000, Seed: 42, Size: 512x256, Model: dreamshaper_8.safetensors, RNG: cuda, Sampler: euler, Version: stable-diffusion.cpp'}
```





