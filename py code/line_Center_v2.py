import time

pid_x = rm_ctrl.PIDCtrl()
pid_y = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_LineList = RmList()

def line_Center_v2(set_time):
    global variable_X
    global variable_Y
    global variable_Post
    global list_LineList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    gimbal_ctrl.pitch_ctrl(-20) 
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    vision_ctrl.enable_detection(rm_define.vision_detection_line) 
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue) 

    pid_Yaw.set_ctrl_params(115,0,5)
    pid_Pitch.set_ctrl_params(85,0,3)
    cnt = 0
    xs = chassis_ctrl.get_position_based_power_on(rm_define.chassis_forward)
    start = time.time()
    while not cnt == 1 and (time.time() - start) <= set_time:
        list_LineList=RmList(vision_ctrl.get_line_detection_info()) 
        #print('time :', time.time() - start)
        if list_LineList[1] >= 1:    
            variable_X = list_LineList[3]
            print(list_LineList[3])  
            variable_Y = list_LineList[4]
            pid_Yaw.set_error(variable_X - 0.5)
            pid_Pitch.set_error(0.5 - variable_Y)
            if list_LineList[3] >= 0.0:
                dy = list_LineList[3] - 0.5 
            else:
                dy = list_LineList[3] + 0.4     
            xk = chassis_ctrl.get_position_based_power_on(rm_define.chassis_forward)
            chassis_ctrl.move_with_speed(xk-xs+0.05, 3 * dy, pid_Yaw.get_output()) 
        else:
            chassis_ctrl.stop()
        list_LineList=RmList(vision_ctrl.get_line_detection_info()) 


def start():
    line_Center_v2(3)