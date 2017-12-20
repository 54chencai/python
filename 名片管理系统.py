# 1. 打印提示
print('==========================')
print('欢迎使用 名片管理系统 v1.0')
print('1. 添加名片')
print('2. 删除名片')
print('3. 修改名片')
print('4. 查看名片')
print('5. 查看所有名字')
print('0. 退出系统')
print('==========================')

card_list = []
while True:
    # 2. 用户选择一个操作
    command = input('请输入要操作的数字: ')
    print('输入的命令是:%s' % command)

    # 3. 判断操作类型
    if command == '1':
        # 添加
        # 获取名字
        new_name = input("请输入一个新的名字: ")
        # 保存名字
        card_list.append(new_name)
        print("新的列表是: %s" % str(card_list))
        pass
    elif command == '2':
        # 删除
        pass
    elif command == '3':
        # 修改
        pass
    elif command == '4':
        # 查看
        find_name = input("请输入要查看的名字:")
        # 判断名字是否存在
        if find_name in card_list:
            print("找到了")
        else:
            print("没找到")
        pass
    elif command == '5':
        # 查看所有

        pass
    elif command == '0':
        # 退出系统
        pass
    else:
        # 输入错误
        pass
