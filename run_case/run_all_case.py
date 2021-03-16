# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/15 10:37 
# ide： PyCharm
import pytest
from common import Shell
# from common.Logs import Email
from common.Logs import Log
import logging

log = Log(__name__)
logger = log.Logger

if __name__ == "__main__":
    # 运行单个文件
    pytest.main(['../test_case/test_login.py'])
    # 运行多个文件
    pytest.main(['../test_case/test_login_getVar.py', '../test_case/test_login.py'])
    # 运行整个目录
    pytest.main(['../test_case', '--html=../report/report.html'])
    logger.info("开始执行脚本")
    try:
        pytest.main(['../test_case/', '--alluredir', '../report/reportalluer'])
        logger.info("脚本执行完成")
    except Exception:
        logger.error("脚本批量执行失败！")
    shell = Shell.Shell()
    cmd = 'allure generate %s -o --clean' % ('../report/reportallure', '../report/reporthtml')
    try:
        logger.info("开始执行报告生成")
        shell.invoke(cmd)
        logger.info("报告生成完毕")
    except Exception:
        logger.error("报告生成失败，请重新执行")
        # log.err('执行用例失败，请检查环境配置')
        raise

