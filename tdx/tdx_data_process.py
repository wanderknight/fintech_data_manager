__author__ = 'wanderknight'
__time__ = '2018/4/29 13:12'
import os
import tqdm

tdx_export_path = ''
tdx2csv_data_path = ''


def tdx_export_txt2csv(export_f, tdx_K_day_path):
    with open(tdx_export_path+export_f, 'r') as f:
        fl = f.readlines()

    csv_name = os.path.split(export_f)[1].replace('.txt', '.csv')
    csv_path_name = os.path.join(tdx_K_day_path, csv_name)
    with open(csv_path_name, 'w') as fp:
        fp.writelines('date,open,high,low,close,volume,amount\n')
        fp.writelines(fl[2:-1])


def init_import_k_data():
    files = os.listdir(tdx_export_path)
    tdx_K_day_path = tdx2csv_data_path + 'tdx\\k_line\\K_day'
    if not os.path.exists(tdx_K_day_path):
        os.makedirs(tdx_K_day_path)
        print(tdx_K_day_path, '创建成功！')
    for export_f in tqdm.tqdm(files):
        tdx_export_txt2csv(export_f, tdx_K_day_path)


def get_status():
    print('hello')
    pass


def update_k_data():
    pass
