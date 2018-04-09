from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import InventoryQueryResponse,Sku,SkuItemId,SkuCategory,SkuWarehouse
from .choice import *
import time
import datetime
def index(request):
    return HttpResponse("Hello, this is used to test the ali mysql")


def daily_check(request):
    bt = time.time()
    # oms每天跟wms核对一下库存数量，并据此进行同步确认。同步的单位是：某个仓库的某件商品。

    owner_list = []
    warehouse_list = []
    item_code_list = []
    bill_list = []
    page_index = 1
    page_size =30
    # 异动源：多个用户，多个仓库，多件商品。
    #----------- 访问表 InventoryQueryResponse 获取全部objects
    print('#1', time.time())
    t1 = time.time()
    report_list = InventoryQueryResponse.objects.all().order_by('-created_at')
    t2 = time.time()
    t_a = (t2 - t1)*1000
    # print(len(report_list))
    #----------- 通过两个栏位查询 --------
    t1 = time.time()
    if 'warehouse_code' in {'warehouse_code':1}:
        report_list = report_list.filter(warehouse_code='cf3c23f41a6142fa9e4d011b71ed8018')
    if 'warehouse_id' in {'warehouse_id':1}:
        report_list = report_list.filter(warehouse_id='WH10000085')
    t2 = time.time()
    t_b = (t2 - t1)*1000
    print('###一',time.time())
    # print(len(report_list))
    # ----------- 通过两个栏位查询 --------
    # ----------- 访问表 InventoryQueryResponse 获取全部objects
    t1 = time.time()
    if len(report_list) == 0:
        return HttpResponse("report_list == 0")
    t2 = time.time()
    print('用在len(report_list)的时间',t2-t1)
    # user_id + item_code 唯一定位一件商品
    #Join 表SkuItemId和表Sku
    t1 = time.time()
    items_list = SkuItemId.objects.all().select_related('sku').\
        order_by('-created_at')
    t2 = time.time()
    t_c = (t2 - t1)*1000
    # Join 表SkuItemId和表Sku
    print(t2,t1)
    print('###二', time.time())
    #通过3个栏位 查询
    t1 = time.time()
    if 'sku_name' in {'sku_name':'sku_name'}:
        items_list = items_list.filter(sku__sku_name__contains='山东老馒头')
    if 'item_code' in {'item_code':1}:
        items_list = items_list.filter(sku__item_code='2160336813')
    if 'bar_code' in {'bar_code':1}:
        items_list = items_list.filter(sku__bar_code='7362737283756')
    t2 = time.time()
    t_d = (t2 - t1)*1000
    print('###三', time.time())
    # 通过3个栏位 查询
    # if 'user_name' in param.keys():
    #     id_list, user_list = get_user_list(nickname=param['user_name'])
    #     items_list = items_list.filter(user_id__in=id_list)
    # if 'user_phone' in param.keys():
    #     id_list, user_list = get_user_list(phone=param['user_phone'])
    #     items_list = items_list.filter(user_id__in=id_list)
    # 如果搜索条件不满足，返回空。
    print('#2', time.time())
    if len(items_list) == 0:
        return HttpResponse("items_list == 0")
    for report in report_list:
        if report.owner_code not in owner_list:
            owner_list.append(report.owner_code)
        if report.warehouse_id not in warehouse_list:
            warehouse_list.append(report.warehouse_id)
        if report.item_code not in item_code_list:
            item_code_list.append(report.item_code)
    print('{0}, {1}, {2}'.format(owner_list, item_code_list, warehouse_list))
    # user_info_list = _get_user_info_list(*owner_list)
    items_list = items_list.filter(user_id__in=owner_list,
                                   item_code__in=item_code_list,
                                   warehouse_id__in=warehouse_list)
    print('report num=', len(items_list))
    print('#3', time.time())
    # 逐件商品查，是否有异动，有则展示最近一次异动记录。前提条件：任何一件商品，都在sku_item_id表中有记录。
    for item in items_list:
        # owner_code + item_code + warehouse_id这三个值才能唯一确定某个仓库中的某件商品.
        _list = report_list.filter(owner_code=item.user_id,
                                   item_code=item.item_code,
                                   warehouse_id=item.warehouse_id).order_by('-created_at')
        if len(_list) == 0:
            continue
        report = _list[0]       # 同一个仓库同一件商品，只需要同步最近一条查询异常记录
        sku_wh = SkuWarehouse.objects.filter(warehouse_id=item.warehouse_id, sku_id=item.sku_id)
        if len(sku_wh) > 0:
            sku_wh_quantity = sku_wh[0].quantity
        else:
            sku_wh_quantity = 0
        shows = {
            # report 是细分到item_code的，因此，report_id可以作为唯一的区分。
            'id': report.id,
            'sku_id': item.sku_id,
            'user_id': item.user_id,
            'warehouse_id': item.warehouse_id,
            'warehouse_code': report.warehouse_code,
            'warehouse_name': report.warehouse_name,
            'sync_status': report.status,
            'sku_name': item.sku.sku_name,
            'sku_specification': item.sku.specification,
            'sku_item_code': item.sku.item_code,
            'sku_bar_code': item.sku.bar_code,
            # 'total_quantity': item.sku.quantity,
            'total_quantity': sku_wh_quantity,
            'quantity_diff': report.quantity_diff,
            'created_at': datetime2timestamp(report.created_at),
            'sync_comments': report.sync_comments,
            # 排序用的字段。
            'abs_diff_quantity': abs(report.quantity_diff),
        }
        # for data in user_info_list:
        #     if data['user_id'] == item.user_id:
        #         shows['user_name'] = data['user_name']
        #         shows['user_phone'] = data['user_phone']
        #         break
        bill_list.append(shows)
    # 排序输出（首先是时间倒序排，然后是变化差值最大倒序排）。
    print('#4', time.time())
    bill_list.sort(key=lambda x: x['abs_diff_quantity'], reverse=True)
    paginator = Paginator(bill_list, page_size)
    try:
        items = paginator.page(int(page_index))
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    print('#5', time.time())
    et = time.time()
    t_e = et - bt
    ##############################################
    #t_a   获取全部InventoryQueryResponse objects的时间
    #t_b   通过两个栏位查询InventoryQueryResponse的时间
    #t_c   获取全部表SkuItemId和表Sku objects的时间
    #t_d   通过三个栏位查询表SkuItemId和表Sku的时间
    #t_e   整个daily_check跑完的时间
    #
    ##############################################

    return HttpResponse("获取全部InventoryQueryResponse objects的时间{}毫秒<br>"
                        "通过两个栏位查询InventoryQueryResponse的时间{}毫秒<br>"
                        "获取全部表SkuItemId和表Sku objects的时间{}毫秒<br>"
                        "通过三个栏位查询表SkuItemId和表Sku的时间{}毫秒<br>"
                        "整个daily_check跑完的时间{}秒".format(t_a,t_b,t_c,t_d,t_e))