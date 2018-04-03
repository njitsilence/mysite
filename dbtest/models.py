# -*- coding: UTF-8 -*-
from django.db import models
from .base import BaseModel
from .choice import *

class Sku(BaseModel):

    UNIT_CHOICES = (
        ('kg.', '千克'),
    )

    id = models.CharField(
        max_length=20,
        primary_key=True,
        verbose_name='sku编码',
        editable=False)

    item_code = models.CharField(null=True, max_length=20, verbose_name='奇门编码')

    outer_item_code = models.\
        CharField(max_length=64, null=True, verbose_name='第三方编码')

    sku_name = models.CharField(max_length=128, verbose_name='商品名称')

    specification = models.CharField(null=True, max_length=128, verbose_name='商品规格')

    bar_code = models.CharField(null=True, max_length=64, verbose_name='商品条码')

    # user_code = models.CharField(max_length=64, verbose_name='商家编码')

    price = models.FloatField(default=0.0, verbose_name='商家价格')

    unit = models.\
        CharField(default='kg', max_length=10, choices=UNIT_CHOICES, verbose_name='商品单位')

    goods_no = models.CharField(null=True, max_length=64, verbose_name='货号')
    sku_version = models.IntegerField(default=0, null=True)
    item_type = models.CharField(null=True, max_length=20, verbose_name='产品类型')

    brand = models.CharField(null=True, max_length=20, verbose_name='产品品牌编码')
    brand_name = models.CharField(null=True, max_length=20, verbose_name='产品品牌名称')
    color = models.CharField(null=True, max_length=10)
    size = models.CharField(null=True, max_length=10)
    gross_weight = models.IntegerField(default=0, verbose_name='毛重，单位克')
    net_weight = models.IntegerField(default=0, verbose_name='净重，单位克')
    length = models.IntegerField(default=0, verbose_name='单位毫米')
    width = models.IntegerField(default=0, verbose_name='单位毫米')
    height = models.IntegerField(default=0, verbose_name='单位毫米')
    volume = models.IntegerField(default=0, verbose_name='单位立方厘米')
    pcs = models.IntegerField(default=0, verbose_name='箱规')

    quantity = models.IntegerField(default=0, verbose_name='Sku数量')

    available_quantity = models.IntegerField(default=0, verbose_name='可用Sku数量')
    is_shelflife = models.BooleanField(default=False, verbose_name='是否启用保质期管理')
    lifecycle = models.IntegerField(default=0, verbose_name='保质期天数')
    reject_lifecycle = models.IntegerField(default=0, verbose_name='保质期禁收天数')
    lockup_lifecycle = models.IntegerField(default=0, verbose_name='保质期禁售天数')
    advent_lifecycle = models.IntegerField(default=0, verbose_name='保质期临期天数')
    is_sn_mgt = models.BooleanField(default=False)
    is_hygroscopic = models.BooleanField(default=False)
    is_danger = models.BooleanField(default=False)

    # 是否存在? 订单中出现了不存在的sku
    is_exist = models.BooleanField(default=True)
    # 增加组合商品标识  lvpeng
    combination_flag = models.BooleanField(default=False, verbose_name='是否是组合商品')
    # 增加虚拟商品标识  lvpeng
    virtual_flag = models.BooleanField(default=False, verbose_name='是否虚拟商品')
    # 关联字段
    category = models.ForeignKey('SkuCategory', null=True, verbose_name='产品类别',on_delete=models.CASCADE)
    category_name = models.CharField(max_length=20, verbose_name='产品类别名称')
    user_id = models.IntegerField(null=False, verbose_name='用户id')
    # owner = models.ForeignKey('oms.User', null=True, verbose_name='所属商户')

    # 覆盖内建的删除方法
    # 检查库存是否为空
    # 在批量删除时，不会调用
    # 需要实现pre_delelte方法
    # def delete(self, *args, **kwargs):
    #     pass

    # def __str__(self):
    #     return self.sku_name

    class Meta:
        ordering = ['-created_at']
        app_label = 'dbtest'
        db_table = 'sku'
        unique_together = (('user_id', 'item_code'),)


class InventoryQueryResponse(BaseModel):

    id = models.AutoField(primary_key=True)

    status = models.CharField(
        max_length=30,
        choices=REPORT_STATUS,
        default=REPORT_STATUS[0][1],
        verbose_name='库存同步状态')
    # ownerCode String 必须 H1234货主编码
    owner_code = models.CharField(max_length=20, verbose_name='货主编码')
    # warehouseCode String 必须 CH1234仓库编码
    warehouse_code = models.CharField(max_length=40, verbose_name='仓库编码')
    warehouse_id = models.CharField(
        max_length=20,
        null=True,
        verbose_name='仓库id')
    warehouse_name = models.CharField(
        max_length=32,
        null=True,
        verbose_name='仓库名称')

    inventory_type = models.CharField(
        max_length=10,
        choices=INVENTORY_TYPE,
        verbose_name='库存类型')

    wms_quantity = models.IntegerField(verbose_name='wms系统商品总量')
    wms_lock_quantity = models.IntegerField(verbose_name='wms系统锁定商品量')
    oms_quantity = models.IntegerField(verbose_name='oms系统商品总量')
    oms_lock_quantity = models.IntegerField(verbose_name='wms系统锁定商品量')
    # wms-oms 差值.wms视角 即 如果wms比oms多5,差值为 +5. 如果wms比mos少5,差值为 -5
    quantity_diff = models.IntegerField(default=0,verbose_name='总库存差值')
    lock_quantity_diff = models.IntegerField(default=0,verbose_name='锁定库存差值')

    item_id = models.CharField(null=True, max_length=40, verbose_name='仓储系统商品ID')
    item_code = models.CharField(null=True, max_length=30, verbose_name='商家编码')

    batch_code = models.CharField(
        max_length=30,
        null=True,
        verbose_name='批次编码')
    product_date = models.DateTimeField(
        null=True,
        verbose_name='商品生产日期(YYYY-MM-DD)')
    expire_date = models.DateTimeField(
        null=True,
        verbose_name='商品过期日期(YYYY-MM-DD)')
    produce_code = models.CharField(
        null=True,
        max_length=30,
        verbose_name='生产批号')

    sync_comments = models.CharField(max_length=100, verbose_name='同步备注', default='')
    operator_id = models.CharField(max_length=30, verbose_name='操作员id', null=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'inventory_query_response'


# 商品目录表
class SkuCategory(BaseModel):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20, verbose_name='目录名称')
    # category_desc = models.CharField(max_length=20, verbose_name='目录描述')

    user_id = models.IntegerField(null=False, verbose_name='用户id')

    super_category = models.\
        ForeignKey('self', null=True, related_name='sub_category',on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.category_name

    class Meta:
        ordering = ['-created_at']
        app_label = 'dbtest'
        db_table = 'oms_sku_category'

class SkuItemId(BaseModel):
    id = models.AutoField(primary_key=True)
    sku = models.ForeignKey('Sku', null=False, verbose_name='关联的商品',on_delete=models.CASCADE)
    warehouse_id = models.\
        CharField(max_length=20, null=False, verbose_name='同步的仓库')
    # user_id = models.IntegerField(null=False, verbose_name='用户id')
    user_id = models.CharField(max_length=20, verbose_name='货主编码即用户id')
    item_code = models.CharField(max_length=64, verbose_name='商家编码')

    item_id = models.CharField(max_length=64, verbose_name='仓库商品编码')

    class Meta:
        db_table = 'sku_item_id'
        unique_together = (('sku', 'warehouse_id'),)

# 库存中间表：多对多
class SkuWarehouse(BaseModel):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0, verbose_name='Sku库存总数量')

    available_quantity = models.IntegerField(default=0, verbose_name='可用Sku库存数量')

    # 下面的几个数据都是仓库在入库的时候测量的，而sku中的数据是从货主那里获得的
    gross_weight = models.IntegerField(default=0, verbose_name='毛重，单位克')
    net_weight = models.IntegerField(default=0, verbose_name='净重，单位克')
    length = models.IntegerField(default=0, verbose_name='单位毫米')
    width = models.IntegerField(default=0, verbose_name='单位毫米')
    height = models.IntegerField(default=0, verbose_name='单位毫米')
    volume = models.IntegerField(default=0, verbose_name='单位立方厘米')

    warehouse_id = models.\
        CharField(max_length=20, null=False, verbose_name='仓库id')

    warehouse_name = models.CharField(max_length=32, verbose_name='仓库名称')

    warehouse_province = models.CharField(max_length=32, null=True, verbose_name='仓库省份')

    warehouse_city = models.CharField(max_length=32, null=True, verbose_name='仓库城市')

    warehouse_area = models.CharField(max_length=32, null=True, verbose_name='仓库地区')

    warehouse_detail = models.CharField(max_length=32, null=True, verbose_name='仓库详细地址')

    warehouse_longitude = models.CharField(max_length=32, null=True, verbose_name='仓库经度')

    warehouse_latitude = models.CharField(max_length=32, null=True, verbose_name='仓库纬度')

    sku = models.ForeignKey('Sku', on_delete=models.CASCADE, verbose_name='Sku')

    user_id = models.IntegerField(null=False, verbose_name='用户id')

    class Meta:
        ordering = ['-created_at']
        app_label = 'dbtest'

    @property
    def warehouse_address(self):
        return self.warehouse_province + self.warehouse_city +\
            self.warehouse_area + self.warehouse_detail

    def __str__(self):
        return '仓库-sku'