from PIL import Image, ImageDraw, ImageFont

draw_image = Image.open("right_switch_recognizer/scheme.png")
font = ImageFont.truetype("right_switch_recognizer/arial.ttf", size=20)
draw_text = ImageDraw.Draw(draw_image)
draw_text.text(
    (850, 580),
    "Включен",
    font=font,
    fill=("#19ff19")
    )
draw_text.text(
    (130, 860),
    "Включен",
    font=font,
    fill=("#19ff19")
    )
draw_image.show()
