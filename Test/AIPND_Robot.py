import random

env_data = [[2, 2, 3, 0, 2, 0],
            [1, 2, 2, 0, 2, 0],
            [0, 0, 2, 0, 2, 0],
            [2, 0, 2, 0, 0, 0],
            [2, 0, 0, 0, 2, 0]]

 #TODO 1模拟环境的行数
rows = len(env_data)

#TODO 2模拟环境的列数
columns = len(env_data[0])

#TODO 3取出模拟环境第三行第六列的元素
row_3_col_6 = env_data[3-1][6-1]

def int_function_barriers_row(data, row):
    line = data[row]
    num = 0
    for item in line:
        if item == 2:
            num += 1
    return num

def int_function_barriers_col(data, col):
    num = 0
    for line in data:
        if line[col] == 2:
            num += 1
    return num

#TODO 4计算模拟环境中，第一行的的障碍物个数。
number_of_barriers_row1 = int_function_barriers_row(env_data, 1 - 1)

#TODO 5计算模拟环境中，第三列的的障碍物个数。
number_of_barriers_col3 = int_function_barriers_col(env_data, 3 - 1)

def tuple_function_find(data, num):
    for row in range(len(data)):
        line = data[row]
        for col in range(len(line)):
            if line[col] == num:
                return (row, col)
    print("Not Found:", num)

#TODO 6按照上述要求创建字典
start = tuple_function_find(env_data, 1)
destination = tuple_function_find(env_data, 3)
loc_map = {"start" : start,
          "destination" : destination}
print("loc_map:", loc_map)

robot_current_loc = loc_map["start"] #TODO 7保存机器人当前的位置
destination_loc = loc_map["destination"] # 保存目标位置

def is_move_valid(env_data, loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    env -- list, the environment data
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    #TODO 9
    row = loc[0]
    col = loc[1]
    if act == "u":
        row -= 1
    if act == "d":
        row += 1
    if act == "l":
        col -= 1
    if act == "r":
        col += 1

    return (0 <= row < rows) and (0 <= col < columns) and env_data[row][col] != 2

    ## TODO 10 从头定义、实现你的函数
def valid_actions(env_data, loc):
    actions = ["u", "d", "l", "r"]
    v_actions = []
    for act in actions:
        can_move = is_move_valid(env_data, loc, act)
        if can_move:
            v_actions.append(act)
    return v_actions

# actions = valid_actions(env_data, robot_current_loc)
# print("acitons:", actions)

##TODO 11 从头定义、实现你的函数
def move_robot(loc, act):
    mov = (0, 0)
    if act == "u":
        mov = (- 1, 0)
    if act == "d":
        mov = (1, 0)
    if act == "l":
        mov = (0, - 1)
    if act == "r":
        mov = (0, 1)

    new_loc = (loc[0] + mov[0], loc[1] + mov[1])
    return new_loc

# robot_current_loc = move_robot(robot_current_loc, "u")
# print("robot_current_loc:", robot_current_loc)

##TODO 12 从头实现你的函数
def random_choose_actions(env_data, loc, times):
    step = 0
    for index in range(times):
        if loc == destination_loc:
            print("在第{}个回合找到宝藏！".format(step))
            return
        else:
            actions = valid_actions(env_data, loc)
            action = random.choice(actions)
            loc = move_robot(loc, action)
            step += 1
    print("未找到宝藏，试试看增大回合数")

##TODO 13 最短路径策略算法
def num_steps(env_data, loc_start, loc_end):
    que = []
    def_value = 0
    step_list = [[def_value for col in range(columns)] for row in range(rows)]

    que.append(loc_start)
    while len(que) > 0:
        print("\nque:", que)

        loc = que[len(que) - 1]
        print("loc:", loc)
        que.pop()
        actions = valid_actions(env_data, loc)
        for action in actions:
            to_loc = move_robot(loc, action)
            print("to_loc:", to_loc)
            step = step_list[loc[0]][loc[1]]
            to_step = step_list[to_loc[0]][to_loc[1]]
            if (to_step == def_value):
                que.append(to_loc)
                row = to_loc[0]
                col = to_loc[1]
                step_list[row][col] = step + 1
            if (to_loc == loc_end):
                print("break")
                break;
    return step_list[loc_end[0]][loc_end[1]]

# 运行
random_choose_actions(env_data, robot_current_loc, 400)

num = num_steps(env_data, robot_current_loc, destination_loc)
print("最少步骤:", num)
