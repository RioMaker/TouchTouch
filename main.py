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
    Plain,
    Image,
    At  # 如果你的框架中用于艾特别人的消息元素叫做别的名字，请自行调整
)

@register(
    name="TouchTouchPlugin", 
    description="摸摸你的", 
    version="1.1", 
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
        功能：
          1) /摸摸           -> 取发送者自己的QQ，发送摸摸图片
          2) /摸摸 @某人     -> 取被@人的QQ，发送摸摸图片
          3) /摸摸 帮助      -> 显示帮助信息
          4) /摸摸 help      -> 显示帮助信息
        """
        # 将消息对象转为字符串，去除左右空白
        msg_str = str(ctx.event.message_chain).strip()
        
        # 判断是否以 "/摸摸" 开头
        if not msg_str.startswith("/摸摸"):
            return  # 不满足则直接返回
        
        # 如果用户输入的是 "/摸摸 帮助" 或 "/摸摸 help"，则输出帮助
        if msg_str in ["/摸摸 帮助", "/摸摸 help"]:
            help_text = (
                "【摸摸插件使用说明】\n"
                "1) 直接发送「/摸摸」，会为自己生成摸摸图片。\n"
                "2) 发送「/摸摸 @某人」，会为该用户生成摸摸图片。\n"
                "3) 发送「/摸摸 帮助」或「/摸摸 help」，查看本帮助。"
            )
            await ctx.reply(
                MessageChain([
                    Plain(help_text)
                ])
            )
            return
        
        # ================ 处理「/摸摸」(可带@) ================

        # 先尝试从消息链中找 `At`（@某人的元素），若未找到则使用发送者自己
        target_qq = None

        for item in ctx.event.message_chain:
            # 如果有 At 类型元素，则取它的 target
            if isinstance(item, At):
                target_qq = item.target
                break
        
        # 若没有在消息里找到 @ 别人，则默认为发送者自己
        if not target_qq:
            target_qq = ctx.event.sender_id
        
        # 构造摸摸图片链接
        image_url = f"https://uapis.cn/api/mt?qq={target_qq}"

        # 发送图片
        await ctx.reply(
            MessageChain([
                Image(url=image_url)
            ])
        )
