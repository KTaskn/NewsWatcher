from os import path
from datetime import datetime, timedelta, timezone
import re
import glob
import pyknp
from bs4 import BeautifulSoup

from api.models import Newspaper, Word

def parse(text):
    obj_juman = pyknp.Juman()
    return map(
        lambda ent: ent.genkei,
        filter(
            lambda ent: ent.hinsi in ['名詞'],
            obj_juman.analysis(text).mrph_list()
        ))

DIC_CLASS = {
    'mainichi': 'main-box',
    'yomiuri': 'uni-home-main',
    'nikkei': 'k-hub-layout__container--headline k-hub-layout__container',
    'asahi': 'Section SectionHomeTop TopNewsArea',
    'sankei': 'column_center',
    'hokkaido': 'mainNews',
    'kahoku': 'mainnews',
    'chunichi': 'l-container',
    'tokyo': 'cmp-m-catelst002',
    'chugoku': 'separate',
    'nishinippon': 'c-articleList',
    'ryukyushimpo': 'pc-page-kvarea',
    'okinawatimes': 'top-side-block',
}
def get_words(path, name_newspaper, encoding='UTF-8'):
    l_output = []
    with open(path, 'r', encoding=encoding) as f:
        rawdata = f.read()
        soup = BeautifulSoup(rawdata, 'html.parser')
        for row in list(map(lambda row: row.text, soup.find_all(class_=DIC_CLASS[name_newspaper]))):
            row = row.replace(' ', '').replace('\t', '').replace('　', '').replace('#', '').replace('\n', '')
            print(row)
            if row:
                l_output += list(parse(row))
    return l_output

def save(date, name_newspaper, words):
    for a_word in words:
        obj_newspaper = Newspaper.objects.get(name=name_newspaper)
        obj = Word(
            newspaper=obj_newspaper,
            _datetime=date,
            word=a_word,
        )
        obj.save()


# mainichi,https://mainichi.jp/
# yomiuri,https://www.yomiuri.co.jp/
# nikkei,https://www.nikkei.com/
# asahi,https://www.asahi.com/
# sankei,https://www.sankei.com/
# hokkaido,https://www.hokkaido-np.co.jp/
# kahoku,https://www.kahoku.co.jp/
# chunichi,https://www.chunichi.co.jp/
# tokyo,https://www.tokyo-np.co.jp/
# chugoku,https://www.chugoku-np.co.jp/
# nishinippon,https://www.nishinippon.co.jp/
# ryukyushimpo,https://ryukyushimpo.jp/
# okinawatimes,https://www.okinawatimes.co.jp/



def run(*args):
    LIST_PASS = ['chugoku']
    LIST_SJIS = ['kahoku', 'chugoku']
    if len(args) > 0:
        _input = args[0]

        PATH_ARCHIVES = '/archives'
        # JST = timezone(timedelta(hours=+9), 'JST')
        dirs = glob.glob(path.join(PATH_ARCHIVES, '%s*') % _input)

        for a_dir in dirs:
            path_file = path.join(a_dir, 'index.html')
            tstr, name_newspaper = path.basename(a_dir).split('_')
            if name_newspaper in LIST_PASS:
                pass
            else:
                if name_newspaper in LIST_SJIS:
                    words = get_words(path_file, name_newspaper, 'shift-jis')
                else:
                    words = get_words(path_file, name_newspaper)
                date = datetime.strptime(tstr, '%Y%m%d%H%M%S')
                save(date, name_newspaper, words)
    else:
        print('引数が存在しない')