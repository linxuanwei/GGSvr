# coding: utf-8
import sys, os
# 脚本路径
SCRIPT_ROOT_PATH = './'

def patch_sys_path():
    sys_paths = []

    def add_path(path):
        paths = os.listdir(path)
        for p in paths:
            abs_path = path + p
            if abs_path[-1] != "/": abs_path += "/"
            if p == ".svn" or not os.path.isdir(abs_path):
                pass        # 过滤掉.svn  文件
            else:
                add_path(abs_path)
                sys_paths.append(abs_path)

    add_path(SCRIPT_ROOT_PATH)

    for p in sys_paths:
        sys.path.insert(0, p)
    print "patch_sys_path() ok"
patch_sys_path()


# ------------------------------
import gconfig, gnet, glog, gdb

def main():

    # 初始化底层库
    # 配置文件
    gconfig.init()

    # 日志
    glog.init()

    # 网络
    gnet.init_sub_server(gconfig.SVR_MAIN_IP, gconfig.SVR_MAIN_PORT, gconfig.SVR_SUB_NAME, gconfig.SVR_SUB_ID)

    # 数据库
    #gdb.init()

    # 测试 client-svr_main-svr_sub
    import svr_test_sub
    svr_test_sub.init()

    # 开始服务
    gnet.start_loop()


if __name__ == "__main__":
    main()



