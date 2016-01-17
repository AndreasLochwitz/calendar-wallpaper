import calendar
from PIL import Image, ImageDraw, ImageFont, ImageFilter

c = calendar.TextCalendar(calendar.MONDAY)
c.prmonth(2016, 1)
cal = calendar.Calendar()

days = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']
i = 0;

scaleFactor = 5

fnt = ImageFont.truetype('miso-light.ttf', 20 * scaleFactor)

fnt_gross = ImageFont.truetype('miso-regular.ttf', size=100 * scaleFactor)

source_image = Image.open("MGL-Logo-Air.png").convert('RGBA')

text_image = Image.new('RGBA', (source_image.size[0] * scaleFactor, source_image.size[1] * scaleFactor), (255,255,255,0))

d = ImageDraw.Draw(text_image)

# d = ImageDraw.Draw(source_image)

d.fontmode = "1"

x_pos = 10 * scaleFactor
y_pos = 20 * scaleFactor
delta_x = 40 * scaleFactor
delta_y = 20 * scaleFactor
alpha = 255

for x in cal.itermonthdays(2016, 1):
    if x > 0:
        # print(x, end=""),
        alpha = 255
        weekday = days[i % 7]
        if weekday == "Sa" or weekday == "So":
            alpha = 150
        d.text((x_pos, y_pos), days[i %7], font=fnt, fill=(255,255,255,alpha))
        d.text((x_pos, y_pos + delta_y), str(x), font=fnt, fill=(255,255,255,alpha))
        x_pos = x_pos + delta_x
    i = i + 1

    d.text((10, -20), 'Januar 2016', font=fnt_gross, fill=(255,255,255,50))

#text_image = text_image.filter(ImageFilter.SMOOTH)
text_image = text_image.resize(source_image.size, Image.ANTIALIAS)

#source_image = source_image.filter(ImageFilter.SMOOTH)

out = Image.alpha_composite(source_image, text_image) #.filter(ImageFilter.GaussianBlur)

out.save('bla.png');

# source_image.show()

# im.show()
