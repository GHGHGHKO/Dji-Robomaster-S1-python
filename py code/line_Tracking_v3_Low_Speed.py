def line_Tracking_v3(set_speed):
    pid_pid = rm_ctrl.PIDCtrl()
    pid_cpst = rm_ctrl.PIDCtrl()
    pid_speed = rm_ctrl.PIDCtrl()
    pid_pitch = rm_ctrl.PIDCtrl()
    pid_Follow_Line = rm_ctrl.PIDCtrl()
    list_LineList = RmList()
    list_MarkerList = RmList()
    list_k = RmList()
    pid_Follow_Line = rm_ctrl.PIDCtrl()
    gimbal_ctrl.set_follow_chassis_offset(0)
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,20)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    pid_Follow_Line.set_ctrl_params(330,0,28)
    time.sleep(0.5)
    cnt = 0
    while not cnt == 1:
        list_LineList=RmList(vision_ctrl.get_line_detection_info())
        if len(list_LineList) == 42: #라인 인식
            #time.sleep(0.5)
            if list_LineList[2] >= 1: #싱글 라인
                
                robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
                variable_x = list_LineList[19]
                pid_Follow_Line.set_error(variable_x - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_Follow_Line.get_output(),0)
                chassis_ctrl.set_trans_speed(set_speed)
                chassis_ctrl.move(0)
                if list_LineList[2] == 2:
                    print('T line')
                    cnt = 1

                if list_LineList[2] == 3:
                    print('+ line')
                    cnt = 1

        else:
            print('no line')
            gimbal_ctrl.rotate_with_speed(0,0)
            cnt = 1

def start():
    line_Tracking_v3(0.3)