# 文字贴图的功能


from PIL import Image, ImageFilter, ImageFont, ImageDraw


class Draw:

    def draw_str(self, img_pos, img, font_pos, text):
        """
        将文字贴入到图片上
        :param img_pos:图片位置
        :param font_pos:文字在图片的位置
        :param text:文字内容
        """
        # img_pos 为待绘画图片位置，font_pos为想要使用的字体路劲，text为想要添加的文字
        image = Image.open(img)  # 打开图片
        dr = ImageDraw.Draw(image)

        font = ImageFont.truetype(font_pos, 60)  # 设置加载字体位置，以及字体大小
        text_bbox = dr.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # 计算居中的x坐标
        x = (image.size[0] - text_width) // 2 + 100
        y = (image.size[1] - text_height) // 2 + 100

        # 在图像上绘制文本
        dr.text((x, y), text, font=font, fill="#ffffff")


        # dr.text((image.size[0] - 300, 150), text, font=font, fill="#000000")  # 设置添加位置、添加内容、以及颜色
        image.save(img_pos + '/assets/' + text + '.jpg')
        # image.show()
