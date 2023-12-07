<!--
 * @Description: 
 * @Author: Panbo Hey
 * @Date: 2023-11-30 16:51:10
 * @LastEditTime: 2023-12-07 10:43:24
 * @LastEditors: Panbo Hey
-->





# AIPROJECTMODULE
POOM的AI中台项目模板




```
cd existing_repo
git remote add origin https://github.com/PANBOHE/AIProjectModule.git
git checkout dev
```



    1. 代码重构和简化:
        将代码分解为更小的函数，每个函数负责一个具体的任务。例如，计算平均温度和湿度、计算高/低温度和湿度的百分比等可以是单独的函数。
        使用更简洁的方式来累加数据，例如使用 Python 的列表推导式。

    2. 数据结构优化:
        考虑使用更高效的数据结构来存储和处理数据。例如，使用 pandas DataFrame 可以简化很多数据处理的操作。

    3. 避免重复代码:
        您的代码中有一些重复的模式，如计算平均值、百分比等。这些可以抽象成单独的函数来避免重复。

    4. 参数检查:
        对输入数据进行有效性检查，确保数据的正确性和完整性。

    5. 异常处理:
        在代码中添加异常处理，特别是在进行数学运算（如除法）时，以避免潜在的错误（例如除以零）。

    6. 命名规范:
        遵循 Python 的命名规范，例如使用 snake_case 命名变量和函数，这将提高代码的可读性。
        变量命名（lower_case_with_underscores）,
        函数命名（lower_case_with_underscores）,
        类命名（CapWords）,
        常量命名（UPPER_CASE_WITH_UNDERSCORES）,
        模块和包命名(config,myconfig,mymodule)

    7. 类型注解:
        使用 Python 的类型注解功能来增强代码的可读性和可维护性。

    8. 文档和注释:
        为函数和类添加文档字符串，说明它们的用途、参数和返回值。

### 2023年12月7日
Author：Panbo
1. 新增/logs/logsfile.py
该模块在项目部署时候针对多个不同的项目使用
2. 新增/core/utils/clear_files_on_time.py
3. 新增main_work.py 包括多线程代码
4. 新增run_work.py 包括python执行脚本问题


### 2023年12月5日
Author: Panbo
1. 新增通过kafka部署模式
2. 新增deploy.py


### 2023年11月29日
Author: Panbo  
1. 模板第一次修改，新增readme，ignore文件
2. 新增logs的文件和修改main当中的示例

