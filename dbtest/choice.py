# -*- coding: utf-8 -*-
import time, datetime

# 订单标注
ORDER_MARK_CHOICE = (
    (10, '正常'),
    (20, '待自动审核'),
    (30, '待人工审核'),
    (40, '锁定'),
    (-1, '关闭')
)

# 订单标注
DELIVERY_CHOICE = (
    (-1, '未发货回传'),
    (0, '发货回传成功'),
    (1, '发货回传失败'),
)

# 订单状态，OMS内部处理用
ORDER_STATUS_CHOICES = (
    (10, '未审核'),
    (20, '已审核'),
    (30, '发货完成'),
    (40, '已签收'),
    (50, '订单取消'),
    (60, '订单删除'),
    (70, '已拆单'),
    (80, '发送wms失败'),
    (90, '订单异常')
)
# 电商平台，退款状态
REFUND_STATUS_CHOICES = (
    (0, '没有退款'),
    (1, '全部退款中或退款成功'),
    (2, '部分退款或退款成功'),
    (3, '退货成功'),
    (4, '部分退货成功'),
    (-1, '退款关闭／拒绝')
)
# refund_status_ori:
# 没有退款：0
# 全部退款成功：1
# 部分退款成功：2
# 退货成功：3
# 部分退货成功：4
# 退款关闭／拒绝：-1

# 电商平台，退货状态
RETURN_STATUS_CHOICES = (
    (0, '没有退货'),
    (1, '退货成功'),
    (2, '部分退货成功'),
    (-1, '退货关闭')
)
# 电商平台，订单状态
ORIGINAL_ORDER_STATUS = (
    (10, '已付款，待发货'),
    (11, '未付款，待发货'),
    (20, '已发货'),
    (21, '已部分发货'),
    (30, '已签收'),
    (31, '已部分签收'),
    (-1, '订单完成/关闭'),
)
# 操作名称编码，代表对订单的各种操作。
OPERATION_CODE = (
    (10, '平台创建订单', '平台接收订单'),
    (11, '订单审核成功', '订单通过系统审核'),
    (12, '订单退出自动审核', '审核失败后转为人工审核'),
    (13, '手动创建订单', '通过操作台手动添加一个订单'),
    (14, '组合商品拆单品', '组合商品拆成单品'),
    (15, '删除订单中的虚拟商品', '删除订单中的虚拟商品'),
    (16, '合并订单中相同的sku', '合并订单中相同的sku'),

    (20, '订单取消', '电商平台在订单为发货完成状态前推送“取消订单”'),
    (21, '订单退款', '电商平台在订单为发货完成状态前推送“订单退款”'),
    (22, '订单修改', '修改订单内容'),
    (23, '订单撤回', '订单从wms撤回，回归待审核状态'),
    (24, '订单自动锁定', '自动锁定：库存不足/欠费/地址异常等其他原因'),
    (25, '订单人工锁定', '人工干预，手动锁定'),
    (26, '订单解锁', '将锁定状态更改为解锁'),
    (27, '订单合并', '将多个订单合并成一个订单，生成新的订单号'),
    (28, '订单拆分', '单一仓库品种不够或数量不够,拆分母订单为多个子订单，生成新的订单号'),
    (29, '仓库未能接单', '仓库接受发货任务失败'),

    (30, '仓库接单', '仓库成功接受发货任务'),
    (31, '发货完成', '仓库出库完成'),
    (32, '退货完成', '客户退货，重新入库'),

    (33, '订单关闭', '人工关闭订单'),
    (34, '订单打印', '订单打印物流单号和分拣单'),
    (35, '订单退款', '订单在完成发货后收到了退款消息，订单转为异常'),
)
# 库存类型
INVENTORY_TYPE = (
    ('ZP', '正品'),
    ('CC', '残次'),
    ('JS', '机损'),
    ('XS', '箱损'),
    ('ZT', '在途库存'),
)
# 库存变化原因
INVENTORY_CHANGE_REASON = (
    (0, 'entry_order', '入库'),
    (1, 'stock_out', '一般出库'),
    (2, 'delivery_order', '销售出库'),
    (3, 'return_order', '退货入库'),
    (4, 'inventory_report', '盘点同步'),
    (5, 'stock_change', '异动同步'),
    (6, 'query_response', '每日查询同步'),
)
# 库存异动处理状态
REPORT_STATUS = (
    ('not_synchronize', '未同步'),
    ('synchronized', '已同步'),
    ('refused', '拒绝')
)

# 为微信小程序添加 状态
STOCK_IN_STATUS = (
    ('NEW', '未开始处理'),
    ('ACCEPT', '仓库接单'),
    ('PARTFULFILLED', '部分收货完成'),
    ('FULFILLED', '收货完成'),
    ('EXCEPTION', '异常'),
    ('CANCELED', '取消'),
    ('CLOSED', '关闭'),
    ('REJECT', '拒单'),
    ('CANCELEDFAIL', '取消失败'),
    ('WITHDRAW','已撤回')
)

# 为微信小程序添加 状态
# ACCEPT=仓库接单,
# PARTFULFILLED-部分收货完成,
# FULFILLED-收货完成,
# PRINT = 打印,
# PICK=捡货,
# CHECK = 复核,
# PACKAGE=打包,
# WEIGH= 称重,
# READY=待提货,
# DELIVERED=已发货,
# REFUSE=买家拒签,
# EXCEPTION =异常，
# CLOSED= 关闭,
# CANCELED= 取消,
# REJECT=仓库拒单
# SIGN=签收
# TMSCANCELED=快递拦截,
# OTHER=其他
# PARTDELIVERED=部分发货完成，
# TMSCANCELFAILED=快递拦截失败,
WMS_STATUS_CHOICE = (
    ('NEW', '未开始处理'),
    ('ACCEPT', '仓库接单'),
    ('PARTDELIVERED', '部分发货完成'),
    ('DELIVERED', '发货完成'),
    ('EXCEPTION', '异常'),
    ('CANCELED', '取消'),
    ('CLOSED', '关闭'),
    ('REJECT', '拒单'),
    ('CANCELEDFAIL', '取消失败'),
    ('PRINT', '打印'),
    ('CHECK', '复核'),
    ('PACKAGE', '打包'),
    ('WEIGH', '称重'),
    ('CANCELEDFA', '取消失败'),     #.. 什么情况
)


ORDER_TYPE = (
    ('JYCK', '一般交易出库单'),  # JYCK=一般交易出库单;
    ('HHCK', '换货出库'),  # HHCK=换货出库;
    ('BFCK', '补发出库'),  # BFCK=补发出库;
    ('PTCK', '普通出库单'),  # PTCK=普通出库单;
    ('DBCK', '调拨出库'),  # DBCK=调拨出库;
    ('B2BRK', 'B2B入库'),  # B2BRK=B2B入库;
    ('B2BCK', 'B2B出库'),  # B2BCK=B2B出库;
    ('QTCK', '其他出库'),  # QTCK=其他出库;
    ('SCRK', '生产入库'),  # SCRK=生产入库;
    ('LYRK', '领用入库'),  # LYRK=领用入库;
    ('CCRK', '残次品入库'),  # CCRK=残次品入库;
    ('CGRK', '采购入库'),  # CGRK=采购入库;
    ('DBRK', '调拨入库'),  # DBRK= 调拨入库;
    ('QTRK', '其他入库'),  # QTRK= 其他入库;
    ('XTRK', '销退入库'),  # XTRK= 销退入库;
    ('HHRK', '换货入库'),  # HHRK= 换货入库;
    ('CNJG', '仓内加工单'),  # CNJG= 仓内加工单
)


def find_name(choice, choice_list):
    for item in choice_list:
        if len(item) > 1 and item[0] == choice:
            return item[1]
    return str(choice)


def find_name2(choice, choice_list):
    for item in choice_list:
        if len(item) > 2 and item[0] == choice:
            return item[1], item[2]
    return str(choice), 'NotFound'


def str_find_name(choice, choice_list):
    for item in choice_list:
        if str(item[0]) == str(choice):
            return str(item[1])
    return str(choice)


def datetime2timestamp(value):
    # Converts a datetime object to UNIX timestamp in milliseconds.
    if value:
        return int(time.mktime(value.timetuple()))
        # return int(time.mktime(value))
