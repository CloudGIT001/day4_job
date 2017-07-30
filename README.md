#### 员工信息表程序，实现增删改查操作：

程序需求
```
可进行模糊查询，语法至少支持下面3种:
	select name,age from staff_table where age > 22
	select  * from staff_table where dept = "IT"
	select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
	UPDATE staff_table SET dept="Market" where dept = "IT"
注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
```

员工信息表文件emp_info.txt：
```
staff_id,name,age,phone,dept,enroll_date
1,xiess,25,12312312312,it,2016-12-12
2,alexli,22,15800220133,it,2013-01-01
3,jackwang,30,13304320533,hr,2015-05-03
4,rainliu,25,1383235322,sales,2016-04-25
5,mackcao,40,1356145343,hr,2009-03-01
```

##### 本程序定位：
本程序用于员工信息管理，实现增删改查的简单操作。

##### 使用说明
```
添加员工信息函数
使用示例：sql>>>:insert into staff_table (name,age,phone,dept,enroll_date) value():mackcao,40,1356145343,hr,2009-03-01
staff_id 为自增，phone做唯一键

删除员工信息函数
使用示例：sql>>>: delete * from staff_table where staff_id = 5
以staff_id 作为删除项

查找员工信息函数
使用示例：
1、sql>>>:select * from staff_table where age > %s(age):25
2、sql>>>:select * from staff_table where dept = %s(dept):hr
3、sql>>>:select * from staff_table where enroll_date like %s(year):2016

修改员工信息函数
使用示例：sql>>>:update staff_table set dept =%s where name = %s (new_dept,name):hr,xiess
```


##### 依赖关系
```
运行环境：
Python3.6

依赖软件包：
from prettytable import PrettyTable
import os
```



##### 问题局限：
```
1、只适合小文件员工信息的管理
2、实现的功能单一

```
