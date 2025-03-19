from pkg.plugin.context import (
    register,
    handler,
    llm_func,
    BasePlugin,
    APIHost,
    EventContext,
)
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import *

api_touch_touch = "https://uapis.cn/api/mt?qq="


# 注册插件
@register(name="TouchTouch", description="摸摸@的人", version="0.5", author="Rio")
class TouchTouchPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = (
            ctx.event.text_message
        )  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        print(msg)
        if msg == "摸摸":
            # ctx.add_return("reply", ["![]({})".format(api_touch_touch+str(ctx.event.sender_id))])
            img_url = api_touch_touch+str(ctx.event.sender_id)
            msg_chain = MessageChain([
                Image(url=img_url)
            ])
            ctx.add_return("reply", msg_chain)
            ctx.prevent_default()
        return

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg_str = str(ctx.event.message_chain).strip()
        if not msg_str:
            return  # 空消息则不处理

        # 确定当前的会话ID（群 or 私聊）
        if hasattr(ctx.event, "group_id") and ctx.event.group_id:
            context_id = f"group_{ctx.event.group_id}"
        else:
            context_id = f"user_{ctx.event.sender_id}"

        parts = msg_str.split(maxsplit=2)
        cmd = parts[0].lstrip("/").lower()

        # /news -> 立即发送一次新闻
        if cmd == "摸摸" and len(parts) == 1:
            await ctx.reply(MessageChain([Image(url=img_url)]))
            return


    # 插件卸载时触发
    def __del__(self):
        pass
