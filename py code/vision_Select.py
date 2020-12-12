import time

pid_x = rm_ctrl.PIDCtrl()
pid_y = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_MarkerList = RmList()

def vision_Select(set_time, set_distance, set_speed, set_number):
    global variable_X
    global variable_Y
    global variable_Post
    global list_MarkerList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    pid_Yaw.set_ctrl_params(115,0,5)
    pid_Pitch.set_ctrl_params(85,0,3)
    cnt = 0
    start = time.time()
    while not cnt == 1 and (time.time() - start) <= set_time:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        #print('time :', time.time() - start)
        if list_MarkerList[1] >= 1 and set_number in list_MarkerList:    
            set_Number_Index = list_MarkerList.index(set_number)
            variable_X = list_MarkerList[set_Number_Index + 1]
            variable_Y = list_MarkerList[set_Number_Index + 2]
            pid_Yaw.set_error(variable_X - 0.5)
            pid_Pitch.set_error(0.5 - variable_Y)
            if list_MarkerList[set_Number_Index + 1] >= 0.0:
                dy = list_MarkerList[set_Number_Index + 1] - 0.5   
            else:
                dy = list_MarkerList[set_Number_Index + 1] + 0.4     
            chassis_ctrl.move_with_speed((set_distance - list_MarkerList[set_Number_Index + 4]) * set_speed, 3 * dy, pid_Yaw.get_output()) 
        else:
            chassis_ctrl.stop()
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())

def start():
    vision_Select(10, 0.4, 3, 13)
