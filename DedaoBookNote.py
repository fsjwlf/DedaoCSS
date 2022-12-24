# Copyright (c) 2022 Fan
# Author: Fan
# Date: 2022.08.09
# Description: 得到电子书笔记导出
# 打开电子书，点击目录，点击笔记，按F12进入DevTools，复制body内容。然后运行本程序，程序自动读取剪贴板内容，然后生成out.html文件，用浏览器打开即可。

import re
import pyperclip

# with open('content.html', 'r', encoding='utf-8') as file:
#     txt = file.read()
txt = pyperclip.paste()

pat = re.compile(r'<div class="reader-note-item"[\s\S]*?class="iget-status"')
txt = pat.findall(txt)[0]  # 提取笔记

pat = re.compile(r'<div (class="reader-note-item-title"[\s\S]*?)</div>')
txt = pat.sub(r'<h1 \1</h1>', txt)  # 设置章节标题

txt = txt.replace('<span class="reader-note-item-title-icon"></span>', '')
txt = txt.replace(' class="reader-note-item-title"', '')
txt = txt.replace(' style="-webkit-box-orient: vertical;"', '')
txt = txt.replace(' <!---->', '')
txt = txt.replace(' class="reader-note-contents"', '')
txt = txt.replace(' class="reader-note-contents-item"', '')
txt = txt.replace(' class="reader-note-contents-item reader-note-contents-note-item"', '')
txt = txt.replace('  ', '')
txt = txt.replace('\n', '')

txt = txt.replace('span', 'em')  # 文字备注
txt = txt.replace('<em>', '<em style="color:red;">')

with open('out.html', 'w', encoding='utf-8') as file:
    print(txt, file=file)
