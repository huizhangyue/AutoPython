# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/12 16:19 
# ide： PyCharm

"""
封装执行 shell 语句方法
"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
