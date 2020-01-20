from PIL import Image
 
def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    
    base_image.save(output_image_path)
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    print("ok")
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)
 

def watermark_with_transparency_center(input_image_path,
                                output_image_path,
                                watermark_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    
    #center position
    
    base_center = (base_image.size[0]/2,base_image.size[1]/2)
    wm_center = (watermark.size[0]/2,watermark.size[1]/2)
    print(base_center, wm_center)
    position = (int(base_center[0]) - int(wm_center[0]),int(base_center[1]) - int(wm_center[1]))
    
    
    #
    base_image.save(output_image_path)
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    print("ok")
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)

 
if __name__ == '__main__':
    img = 'conector.jpg'
#     watermark_with_transparency(img, 'img_wm.png',
#                                 'wm.png', position=(0,0))
    watermark_with_transparency_center(img, str.split(img,'.')[0] + '_wm.png',
                                'wm.png')
    
