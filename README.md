# open-auto-health
> 东北大学学生防控信息统计系统自动化打卡脚本


## 目录

- [使用须知](#使用须知)
- [功能](#功能)
- [自动打卡步骤](#自动打卡步骤) 
- [更新步骤](#更新步骤)
  - [自动打卡](#自动打卡)
- [停止使用](#停止使用)
- [开源协议](#开源协议)

## 使用须知

一切风险与后果由使用者自己承担，与作者无关。

还有这个说明书我没太好好写 卡关了请联系本人

还有你得先注册账号

## 功能

1. 只需要账号和密码
2. 定时每天的北京时间6点进行健康打卡
3. 支持打卡/上报体温后邮件通知(非SSL)//暂时未实装

## 自动打卡步骤
1. Fork本项目

2. 前往Fork后的项目的`Settings`页面

3. 侧边栏点击`Secrets`

4. 通过`add a new secret`添加自己的如下信息（冒号前面的是需要添加的secret的`Name`，后面是对应的`Value`的含义）
  
    - `USER`: 学号
    - `PASS`: 密码
    - `FLAG`: 如果未激活NEU邮箱请设为1，已激活邮箱请设为0
    - 若不清楚自己是否激活邮箱请前往 https://e-report.neu.edu.cn/notes/create 进行查询

    <p align="center"><img src="https://i.loli.net/2020/02/24/RAPvJ4qu5hUIr2K.png"/></p>
    
    全部设置好之后应该是这样的:
    
    <p align="center"><img src="https://i.loli.net/2020/04/17/xIh7gyWUOTR5LAq.png"/></p>
    
5. **进入Fork后的项目的`Actions`页面，如果有 `I understand my workflows, go ahead and run them`按钮，请点击确认**

6. 为了激活自动签到，还需要提交一次commit，流程如下: 

    1. 点击`README.md`的编辑按钮

        <p align="center"><img src="https://i.loli.net/2020/03/01/8pnrtNDm9axih7U.png"/></p>
    
    2. 对内容随意做修改，只要有改动就行
    
    3. 点击编辑框下方的绿色按钮提交改动，就可以激活自动签到任务。
    
        <p align="center"><img src="https://i.loli.net/2020/03/01/6Yi59OyLwQRuVNm.png"/></p>

7. 完成，以防万一还是需要关注邮件或导员通知



## 更新步骤

### 自动打卡

- 重新Fork版 

    1. 删除Fork后的项目，步骤如下
       1. 进入Fork后的项目仓库，进入`Settings`页面
       2. 在最底下找到`Delete this repository`，点击验证后删除
    2. 重新Fork本项目，接下来的步骤同[自动打卡步骤](#自动打卡步骤)

## 停止使用

1. 进入Fork后的项目的`Settings`页面
2. 点击左侧侧边栏的 `Actions`进入设置页面
3. 选择`Disable Actions for this repository `即可禁用掉自动打卡

当然，也可以直接删除Fork后的仓库


## 鸣谢

@unbyte

## 开源协议

MIT License.
