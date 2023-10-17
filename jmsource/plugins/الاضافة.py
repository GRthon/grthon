import asyncio

from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from jmsource import jmsource

from ..core.managers import edit_delete, edit_or_reply


@jmsource.ar_cmd(pattern="انضمام ([\s\S]*)")
async def lol(event):
    bol = event.pattern_match.group(1)
    sweetie = "- جاري الانضمام الى المجموعة انتظر قليلا  ."
    await event.reply(sweetie, parse_mode=None, link_preview=None)
    try:
        await jmsource(functions.channels.JoinChannelRequest(bol))
        await event.edit("**- تم الانضمام بنجاح  ✓**")
    except Exception as e:
        await event.edit(str(e))


@jmsource.ar_cmd(pattern="اضافه ([\s\S]*)")
async def _(event):
    to_add_users = event.pattern_match.group(1)
    if not event.is_channel and event.is_group:
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                    )
                )
            except Exception as e:
                return await edit_delete(event, f"`{str(e)}`", 5)
    else:
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.channels.InviteToChannelRequest(
                        channel=event.chat_id, users=[user_id]
                    )
                )
            except Exception as e:
                return await edit_delete(event, f"`{e}`", 5)

    await edit_or_reply(event, f"**{to_add_users} تم اضافته بنجاح ✓**")


@jmsource.ar_cmd(pattern="ضيف ([\s\S]*)", groups_only=True)
async def get_users(event):
    legen_ = event.text[10:]
    jmsource_chat = legen_.lower
    restricted = ["@YYB6BB", "@G_R_support"]
    jmsource = await edit_or_reply(event, f"**جارِ اضأفه الاعضاء من  ** {legen_}")
    if jmsource_chat in restricted:
        return await jmsource.edit(
            event, "**- لا يمكنك اخذ الاعضاء من مجموعه السورس العب بعيد ابني  :)**"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await jmsource.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    else:
        await jmsource.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    if event.is_private:
        return await jmsource.edit("- لا يمكنك اضافه الاعضاء هنا")
    s = 0
    f = 0
    error = "None"
    await jmsource.edit(
        "**▾∮ حالة الأضافة:**\n\n**▾∮ تتم جمع معلومات المستخدمين 🔄 ...⏣**"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await jmsource.edit(
                    f"**حالة الأضافة انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await jmsource(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await jmsource.edit(
                f"**▾∮تتم الأضافة **\n\n• اضيف `{s}` \n•  خطأ بأضافة `{f}` \n\n**× اخر خطأ:** `{error}`"
            )
            await asyncio.sleep(60)
        except Exception as e:
            error = str(e)
            f = f + 1
    return await jmsource.edit(
        f"**▾∮اڪتملت الأضافة ✅** \n\n• تم بنجاح اضافة `{s}` \n• خطأ بأضافة `{f}`"
    )
