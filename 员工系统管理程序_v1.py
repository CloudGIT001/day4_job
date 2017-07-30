#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen


from prettytable import PrettyTable
import os


def add_emp_info():
    """
    添加员工信息函数
    使用示例：sql>>>:insert into staff_table (name,age,phone,dept,enroll_date) value():mackcao,40,1356145343,hr,2009-03-01
    staff_id 为自增，phone做唯一键
    :return:
    """
    flag = True
    while flag:

        choice = input("[q：返回主菜单；1:创建员工信息>>>:")

        if choice == "1":

            add_info_com = input("sql>>>:insert into staff_table (name,age,phone,dept,enroll_date) value():")
            user_info = add_info_com.split(",")
            # print(user_info[2])

            if len(user_info) == 5:
                with open("emp_info.txt","r+",encoding="utf-8") as f0:
                    list = []
                    for line in f0:
                        s = line.strip().split(",")
                        m = s[3]
                        list.append(m)

                    if user_info[2] in list:
                        print ("\033[31;1m该用户已经存在\033[0m")
                        continue

                    else:
                        index = str(len(list)+1)
                        user_info.insert(0,index)
                        user_info = ','.join(user_info)

                    f0.write("\n")
                    f0.write(user_info)
                    print ("\033[31;1m Query OK, 0 rows affected (0.20 sec)\033[0m")
                    continue

        if choice == "q":
            break

        else:
            print ("\033[41;1m 输入不合法，请重新输入\033[0m")


def del_emp_info():
    """
    删除员工信息函数
    使用示例：sql>>>: delete * from staff_table where staff_id = 5
    以staff_id 作为删除项
    :return:
    """
    flag = True
    while flag:

        choice = input("[q：返回主菜单；1:删除员工信息>>>:")

        if choice == "1":

            def_info_com = input("sql>>>: delete * from staff_table where staff_id = ")
            user_info = def_info_com.split(" ")

            with open("emp_info.txt","r+",encoding="utf-8") as f1_r:
                with open("new_emp_info.txt","w+",encoding="utf-8") as f1_w:
                    if def_info_com == ('%s'%(user_info[0])):
                        for line in f1_r:
                            i = line.strip().split(",")
                            if i[0] != user_info[0]:
                                i = ','.join(i)
                                f1_w.write(i)
                                f1_w.write("\n")
                            else:
                                continue
                        print ("\033[31;1m Query OK, 0 rows affected (0.20 sec)\033[0m")
                        continue

            os.remove("emp_info.txt")
            os.rename("new_emp_info.txt", "emp_info.txt")

        if choice == "q":
            break

        else:
            print ("\033[41;1m 输入不合法，请重新输入\033[0m")


def select_emp_info():
    """
    查找员工信息函数
    使用示例：
    1、sql>>>:select * from staff_table where age > %s(age):25
    2、sql>>>:select * from staff_table where dept = %s(dept):hr
    3、sql>>>:select * from staff_table where enroll_date like %s(year):2016
    :return:
    """
    flag = True
    while flag:
        choice = input("[q：返回主菜单；1:年龄筛选；2：部门筛选；3：登记时间筛选]>>>:")

        if choice == "1":
            select_info_com = input("sql>>>:select * from staff_table where age > %s(\033[31;1mage\033[0m):")
            user_info = select_info_com.split(" ")
            if select_info_com == user_info[0]:
                with open("emp_info.txt", "r+", encoding="utf-8") as f:
                    list1 = []
                    count = 0
                    for line in f:
                        i = line.strip().split(',')
                        if i[2] > user_info[0]:
                            list1.append(i)

                    print(list1[1:])
                    continue

        if choice == "2":
            select_info_com = input("sql>>>:select * from staff_table where dept = %s(\033[31;1mdept\033[0m):").lower()
            user_info = select_info_com.split(" ")
            if select_info_com == user_info[0]:
                with open("emp_info.txt", "r+", encoding="utf-8") as f:
                    list2 = []
                    # count = 0
                    for line in f:
                        i = line.strip().split(',')
                        if i[4] == user_info[0]:
                            list2.append(i)

                    print(list2)
                    continue

        if choice == "3":
            select_info_com = input("sql>>>:select * from staff_table where enroll_date like %s(\033[31;1myear\033[0m):")
            user_info = select_info_com.split(" ")
            if select_info_com == user_info[0]:
                with open("emp_info.txt", "r+", encoding="utf-8") as f:
                    list3 = []
                    list4 = []
                    count = 0
                    for line in f:
                        i = line.strip().split(',')
                        list3.append(i)
                    for j in list3:
                        m = j[5].split('-')
                        if m[0] == user_info[0]:
                            list4.append(j)
                    print(list4)
                    continue

        if choice == "q":
            break

        else:
            print("\033[41;1m 输入不合法，请重新输入\033[0m")


def update_emp_info():
    """
    修改员工信息函数
    使用示例：sql>>>:update staff_table set dept =%s where name = %s (new_dept,name):hr,xiess
    :return:
    """
    flag = True
    while flag:

        choice = input("[q：返回主菜单；1:修改员工信息>>>:")

        if choice == "1":

            update_info_com = input("sql>>>:update staff_table set dept =%s where name = %s (\033[31;1mnew_dept\033[0m,\033[32;1mname\033[0m):")
            user_info = update_info_com.split(",")

            if len(user_info) == 2:
                with open("emp_info.txt","r+",encoding="utf-8") as f3_r:
                    with open("new_emp_info.txt", "w+", encoding="utf-8") as f3_w:
                        for line in f3_r:
                            i = line.strip().split(",")
                            if i[1] == user_info[1]:
                                i[4] = user_info[0]
                                f3_w.write(line)
                            else:
                                f3_w.write(line)
                                continue
            print("\033[31;1m Query OK, 0 rows affected (0.20 sec)\033[0m")
            os.remove("emp_info.txt")
            os.rename("new_emp_info.txt", "emp_info.txt")
            continue

        if choice == "q":
            break

        else:
            print("\033[41;1m 输入不合法，请重新输入\033[0m")


def main():
    """
    主函数，打印主菜单操作
    :return:
    """

    operation = {"1": ["创建员工信息", add_emp_info],
                 "2": ["删除员工信息", del_emp_info],
                 "3": ["查找员工信息", select_emp_info],
                 "4": ["修改员工信息", update_emp_info]}

    oper_list = PrettyTable(["序号","内容"])
    oper_list.padding_width = 4
    oper_list.add_row([0, "退出程序"])
    oper_list.add_row([1, operation["1"][0]])
    oper_list.add_row([2, operation["2"][0]])
    oper_list.add_row([3, operation["3"][0]])
    oper_list.add_row([4, operation["4"][0]])

    flag = True
    while flag:
        print ("主菜单操作:\n",oper_list)
        action_oper = input("请选择你的操作:").strip()

        if action_oper == "1":
            add_emp_info()

        if action_oper == "2":
            del_emp_info()

        if action_oper == "3":
            select_emp_info()

        if action_oper == "4":
            update_emp_info()

        elif action_oper == "0":
            flag = False

if __name__ == "__main__":
    print("\n\033[31;1m欢迎使用员工信息表程序\033[0m\n")
    main()