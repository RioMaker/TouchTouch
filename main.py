from pkg.plugin.context import (
    BasePlugin,
    EventContext,
    register,
    handler,
)
from pkg.plugin.events import (
    GroupMessageReceived,
    PersonMessageReceived
)
from pkg.platform.types import (
    MessageChain,
    Image
)

@register(
    name="TouchTouchPlugin", 
    description="摸摸你的", 
    version="1.0", 
    author="Rio"
)
class MoMoPlugin(BasePlugin):
    
    async def initialize(self):
        print("[TouchTouchPlugin] 插件初始化完成")

    async def on_destroy(self):
        print("[TouchTouchPlugin] 插件销毁")
    
    @handler(PersonMessageReceived)
    @handler(GroupMessageReceived)
    async def on_message(self, ctx: EventContext):
        """
        当检测到消息中有 /摸摸 指令时：
         - 取到发送者的 QQ 号
         - 拼出链接 https://uapis.cn/api/mt?qq=xxxx
         - 回复一张图片
        """
        # 将消息对象转为字符串，去除左右空白
        msg_str = str(ctx.event.message_chain).strip()
        
        # 简单判断，如果等于 "/摸摸" 就执行回复逻辑
        if msg_str == "/摸摸":
            # 取得该用户 QQ
            qq_id = ctx.event.sender_id  # 对私聊和群聊都适用
            
            # 构造图片链接
            image_url = f"https://uapis.cn/api/mt?qq={qq_id}"
            
            # 发送图片
            await ctx.reply(
                MessageChain([
                    Image(url=image_url)
                ])
            )
