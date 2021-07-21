# Thanks Full To Team Ultroid
#
# Geez - Projects <https://github.com/Vckyou/Geez-UserBot/>
# Ported By Vcky @VckyouuBitch
# Copyright (c) 2021 Geez - Projects
# Hasil nyolong karya orang tanpa ijin hehe




import os
import random

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument

from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


PICS_STR = []


@register(outgoing=True, pattern="^.logo(?: |$)(.*)")
async def _(kaisarevent):
    event = await kaisarevent.edit("`Processing.....`")
    fnt = await get_font_file(kaisarevent.client, "@GeezProjectFONT")
    if kaisarevent.reply_to_msg_id:
        rply = await kaisarevent.get_reply_message()
        logo_ = await rply.download_media()
    else:
        async for i in event.client.iter_messages("@GeezLogo", filter=InputMessagesFilterPhotos):
            PICS_STR.append(i)
        pic = random.choice(PICS_STR)
        logo_ = await pic.download_media()
    text = kaisarevent.pattern_match.group(1)
    if len(text) <= 8:
        font_size_ = 150
        strik = 10
    elif len(text) >= 9:
        font_size_ = 50
        strik = 5
    else:
        font_size_ = 130
        strik = 20
    if not text:
        await event.delete("**Berikan Kaisar text untuk di buat logo !!**")
        return
    img = Image.open(logo_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fnt, font_size_)
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        text,
        font=font,
        fill=(255, 255, 255),
    )
    w_ = (image_width - w) / 2
    h_ = (image_height - h) / 2
    draw.text((w_, h_), text, font=font, fill="white",
              stroke_width=strik, stroke_fill="black")
    file_name = "KaisarBot.png"
    img.save(file_name, "png")
    CAPT = f"**Created By** {DEFAULTUSER}"
    await event.client.send_file(
        kaisarevent.chat_id,
        file_name,
        caption=CAPT,
    )
    await event.delete()
    try:
        os.remove(file_name)
        os.remove(fnt)
        os.remove(logo_)
    except BaseException:
        pass


async def get_font_file(client, channel_id):
    font_file_message_s = await event.client.get_reply_message(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None,
    )
    font_file_message = random.choice(font_file_message_s)

    return await event.client.download_media(font_file_message)



CMD_HELP.update({
    "LOGO":
    "`.logo`\
\nUsage: Membuat logo dengan teks yang diberikan. Jika membalas gambar membuat logo yang lain mendapat BG acak.""
})
