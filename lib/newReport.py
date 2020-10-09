#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 16:42
# @Author  : XiaomeiLu
# @FileName: newReport.py
# @Software: PyCharm

import os


def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    return file_new