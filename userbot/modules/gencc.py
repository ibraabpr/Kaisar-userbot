
from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.gencc(?: |$)(.*)")
async def gencc(kenkanaswevent):
    if kenkanaswevent.fwd_from:
        return
    kenkanaswcc = Faker()
    kenkanaswname = kenkanaswcc.name()
    kenkanaswadre = kenkanaswcc.address()
    kenkanaswcard = kenkanaswcc.credit_card_full()

    await edit_or_reply(kenkanaswevent, f"__**👤 NAMA :- **__\n`{kenkanaswname}`\n\n__**🏡 ALAMAT :- **__\n`{kenkanaswadre}`\n\n__**💸 KARTU :- **__\n`{kenkanaswcard}`")


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def bin(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/bin {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.vbv(?: |$)(.*)")
async def vbv(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/vbv {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.key(?: |$)(.*)")
async def key(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/key {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.iban(?: |$)(.*)")
async def iban(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/iban {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.ccheck(?: |$)(.*)")
async def ccheck(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Pengecekan...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/ss {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.ccbin(?: |$)(.*)")
async def ccbin(event):
    if event.fwd_from:
        return
    kenkanasw_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f" Mencoba menghasilkan CC dari bin yang diberikan `{kenkanasw_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1641726479))
            await event.client.send_message(chat, f"/gen {kenkanasw_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "ccarder": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gencc`\
\n : Menghasilkan CC Palsu.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ccheck` <query>\
\n : Memeriksa Apakah CC yang Diberikan Aktif atau Tidak.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.iban` <kueri>\
\n : Memeriksa Apakah ID IBAN yang Diberikan Aktif atau Tidak.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.key` <kueri>\
\n : Memeriksa status kunci yang diprobid.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vbv` <kueri>\
\n : Memeriksa status vbv dari kartu yang diberikan.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bin` <kueri>\
\n : Memeriksa apakah bin yang diberikan valid atau tidak.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ccbin` <bin>\
\n : Menghasilkan CC dari bin yang diberikan."
})
