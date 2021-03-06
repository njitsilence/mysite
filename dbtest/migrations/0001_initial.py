# Generated by Django 2.0.3 on 2018-04-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.NullBooleanField(default=False, verbose_name='是否删除')),
                ('id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False, verbose_name='sku编码')),
                ('item_code', models.CharField(max_length=20, null=True, verbose_name='奇门编码')),
                ('outer_item_code', models.CharField(max_length=64, null=True, verbose_name='第三方编码')),
                ('sku_name', models.CharField(max_length=128, verbose_name='商品名称')),
                ('specification', models.CharField(max_length=128, null=True, verbose_name='商品规格')),
                ('bar_code', models.CharField(max_length=64, null=True, verbose_name='商品条码')),
                ('price', models.FloatField(default=0.0, verbose_name='商家价格')),
                ('unit', models.CharField(choices=[('kg.', '千克')], default='kg', max_length=10, verbose_name='商品单位')),
                ('goods_no', models.CharField(max_length=64, null=True, verbose_name='货号')),
                ('sku_version', models.IntegerField(default=0, null=True)),
                ('item_type', models.CharField(max_length=20, null=True, verbose_name='产品类型')),
                ('brand', models.CharField(max_length=20, null=True, verbose_name='产品品牌编码')),
                ('brand_name', models.CharField(max_length=20, null=True, verbose_name='产品品牌名称')),
                ('color', models.CharField(max_length=10, null=True)),
                ('size', models.CharField(max_length=10, null=True)),
                ('gross_weight', models.IntegerField(default=0, verbose_name='毛重，单位克')),
                ('net_weight', models.IntegerField(default=0, verbose_name='净重，单位克')),
                ('length', models.IntegerField(default=0, verbose_name='单位毫米')),
                ('width', models.IntegerField(default=0, verbose_name='单位毫米')),
                ('height', models.IntegerField(default=0, verbose_name='单位毫米')),
                ('volume', models.IntegerField(default=0, verbose_name='单位立方厘米')),
                ('pcs', models.IntegerField(default=0, verbose_name='箱规')),
                ('quantity', models.IntegerField(default=0, verbose_name='Sku数量')),
                ('available_quantity', models.IntegerField(default=0, verbose_name='可用Sku数量')),
                ('is_shelflife', models.BooleanField(default=False, verbose_name='是否启用保质期管理')),
                ('lifecycle', models.IntegerField(default=0, verbose_name='保质期天数')),
                ('reject_lifecycle', models.IntegerField(default=0, verbose_name='保质期禁收天数')),
                ('lockup_lifecycle', models.IntegerField(default=0, verbose_name='保质期禁售天数')),
                ('advent_lifecycle', models.IntegerField(default=0, verbose_name='保质期临期天数')),
                ('is_sn_mgt', models.BooleanField(default=False)),
                ('is_hygroscopic', models.BooleanField(default=False)),
                ('is_danger', models.BooleanField(default=False)),
                ('is_exist', models.BooleanField(default=True)),
                ('combination_flag', models.BooleanField(default=False, verbose_name='是否是组合商品')),
                ('virtual_flag', models.BooleanField(default=False, verbose_name='是否虚拟商品')),
                ('category_name', models.CharField(max_length=20, verbose_name='产品类别名称')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
