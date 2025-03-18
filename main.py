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
@register(name="TouchTouch", description="摸摸@的人", version="0.1", author="Rio")
class MyPlugin(BasePlugin):

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
            msg_chain = MessageChain([
                Plain("Hello LangBot"),
                Image(url='https://qchatgpt.rockchin.top/langbot-logo.png')
            ])
            ctx.add_return("reply", [msg_chain])
            ctx.prevent_default()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = (
            ctx.event.text_message
        )  # 这里的 event 即为 GroupNormalMessageReceived 的对象
        print(msg)
        if msg == "摸摸":
            # ctx.add_return("reply", ["![]({})".format(api_touch_touch+str(ctx.event.sender_id))])
            msg_chain = MessageChain([
                Plain("Hello LangBot"),
                Image(url='https://qchatgpt.rockchin.top/langbot-logo.png')
            ])
            ctx.add_return("reply", [msg_chain])
            ctx.prevent_default()
        # if msg == "hello":  # 如果消息为hello

        #     # 输出调试信息
        #     self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))

        #     # 回复消息 "hello, everyone!"
        #     ctx.add_return("reply", ["hello, everyone!"])

        #     # 阻止该事件默认行为（向接口获取回复）
        #     ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
