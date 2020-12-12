get_Detection_Number = 0

def turn_Func(set_speed, set_rotate, set_angle, set_sleep):
    while True:
        chassis_ctrl.set_rotate_speed(set_speed)
        if set_rotate == 1:
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, set_angle)
            time.sleep(set_sleep)
            return
        else:
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, set_angle)
            time.sleep(set_sleep)
            return

def line_Tracking():
    pid_pid = rm_ctrl.PIDCtrl()
    pid_cpst = rm_ctrl.PIDCtrl()
    pid_speed = rm_ctrl.PIDCtrl()
    pid_pitch = rm_ctrl.PIDCtrl()
    pid_Follow_Line = rm_ctrl.PIDCtrl()
    list_LineList = RmList()
    list_MarkerList = RmList()
    list_k = RmList()
    list_m = RmList()
    variable_V_average = 0
    variable_shotTime = 0
    variable_device_qn = 0
    variable_markerPosX = 0
    variable_theta = 0
    variable_markerPosY = 0
    variable_max = 0
    variable_Maker = 0
    variable_b = 0
    variable_mode = 0
    variable_c = 0
    variable_pidout = 0
    variable_pitchVal = 0
    variable_n = 0
    variable_markerSizeW = 0
    variable_MarkerSizeH = 0
    variable_i = 0
    variable_x = 0
    variable_X = 0
    variable_Y = 0
    variable_K = 0
    variable_v = 0
    media_ctrl.zoom_value_update(1)
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,20)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(1)
    variable_V_average = 1
    variable_K = 0.65
    pid_Follow_Line.set_ctrl_params(330,0,28)
    while True:
        list_LineList=RmList(vision_ctrl.get_line_detection_info())
        #if len(list_LineList) == 42:
        if list_LineList[1] >= 1:   
            if list_LineList[1] == 2:
                print('T Line')
                chassis_ctrl.stop()
                #rmexit()
                return
            if list_LineList[1] == 3:
                print('+ Line')
                chassis_ctrl.stop()
                return
                #rmexit()
            print('single Line')
            robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
            variable_x = list_LineList[19]
            pid_Follow_Line.set_error(variable_x - 0.5)
            gimbal_ctrl.rotate_with_speed(pid_Follow_Line.get_output(),0)
            variable_v = variable_V_average - variable_K * abs(list_LineList[37] / 180)
            chassis_ctrl.set_trans_speed(variable_v)
            chassis_ctrl.move(0)
            #return

        else:
            gimbal_ctrl.rotate_with_speed(0,0)
            chassis_ctrl.stop()
            return

def move_Axis(set_speed, set_angle, set_distance, set_sleep):
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_trans_speed(set_speed)
    chassis_ctrl.move_with_distance(set_angle, set_distance)
    time.sleep(set_sleep)

def number_Detection(set_distance):
    while True:
        chassis_ctrl.stop()
        pid_gimbal_ctrl.set_follow_chassis_offset(0)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.set_marker_detection_distance(set_distance)
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_zero):
            get_Detection_Number = 0
            return 0
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
            get_Detection_Number = 1
            return 1
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
            get_Detection_Number = 2
            return 2
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
            get_Detection_Number = 3
            return 3
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four):
            get_Detection_Number = 4
            return 4
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_five):
            get_Detection_Number = 5
            return 5
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_six):
            get_Detection_Number = 6
            return 6
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_seven):
            get_Detection_Number = 7
            return 7
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_eight):
            get_Detection_Number = 8
            return 8
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_nine):
            get_Detection_Number = 9
            return 9

 #라인 따라가는 코드
def test():
    variable_X = 0
    list_LineList = RmList()
    pid_Test = rm_ctrl.PIDCtrl()
    variable_Turned = 0
    variable_Turn2 = -5
    variable_V_average = 1
    variable_K = 0.65
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    pid_Test.set_ctrl_params(330,0,28)# 330, 0, 28
    vision_ctrl.enable_detection(rm_define.vision_detection_line) #라인 따라가기 
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue) #파란색 따라가기
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    while True:
        list_LineList=RmList(vision_ctrl.get_line_detection_info()) #라인 정보 파악 
        if len(list_LineList) == 42: #라인 인식됨 
            if list_LineList[2] >= 1: # 0=no line, 1=single line, 2= T-intersection, 3= 4-way intersection
                if list_LineList[2] == 2:
                    print('T Line')
                    chassis_ctrl.stop()
                    #rmexit()
                    return
                if list_LineList[2] == 3:
                    print('+ Line')
                    chassis_ctrl.stop()
                    return
                    #rmexit()
                #print(list_LineList[2])
                variable_X = list_LineList[19]
                pid_Test.set_error(variable_X - 0.5) #0.5
                gimbal_ctrl.rotate_with_speed(pid_Test.get_output(),0)
                variable_v = variable_V_average - variable_K * abs(list_LineList[37] / 180)
                #print('variable_v = ', variable_v)
                chassis_ctrl.set_trans_speed(variable_v / 2)
                chassis_ctrl.move(0)
                #chassis_ctrl.set_trans_speed(0.3) #0.3 | 속도 조절 
                #chassis_ctrl.set_trans_speed(0.3 - abs(list_LineList[9]))
                #chassis_ctrl.move(0)
                time.sleep(0.5)

                #robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
                #variable_x = list_LineList[19]
                #pid_Follow_Line.set_error(variable_x - 0.5)
                #gimbal_ctrl.rotate_with_speed(pid_Follow_Line.get_output(),0)
                

        else: #라인 인식되지 않음
            chassis_ctrl.stop()
            gimbal_ctrl.rotate_with_speed(0,0) #인식을 못했을경우 회전
            time.sleep(0.5) #라인 감지 속도 
            return

#라인 따라가는 코드
pid_Test = rm_ctrl.PIDCtrl()
list_LineList = RmList()
variable_X = 0
variable_Turned = 0
variable_Turn2 = 0

def test2():
    global variable_X
    global list_LineList
    global pid_Test
    variable_Turned = 0
    variable_Turn2 = -5
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    pid_Test.set_ctrl_params(330,0,28)# 330, 0, 28
    vision_ctrl.enable_detection(rm_define.vision_detection_line) #라인 따라가기 
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue) #파란색 따라가기
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    while True:
        list_LineList=RmList(vision_ctrl.get_line_detection_info()) #라인 정보 파악 
        if len(list_LineList) == 42: #라인 인식됨 
            if list_LineList[2] <= 1: # 0=no line, 1=single line, 2= T-intersection, 3= 4-way intersection
                if list_LineList[1] <= 2:
                    print('T Line')
                    chassis_ctrl.stop()
                    #rmexit()
                    return
                if list_LineList[1] <= 3:
                    print('+ Line')
                    chassis_ctrl.stop()
                    return
                    #rmexit()
                #print(list_LineList[2])
                variable_X = list_LineList[19]
                pid_Test.set_error(variable_X - 0.5) #0.5
                gimbal_ctrl.rotate_with_speed(pid_Test.get_output(),0)
                #variable_v = variable_V_average - variable_K * abs(list_LineList[37] / 180)
                #print('variable_v = ', variable_v)
                #chassis_ctrl.set_trans_speed(variable_v / 2)
                chassis_ctrl.set_trans_speed(0.3)
                chassis_ctrl.move(0)
                #chassis_ctrl.set_trans_speed(0.3) #0.3 | 속도 조절 
                #chassis_ctrl.set_trans_speed(0.3 - abs(list_LineList[9]))
                #chassis_ctrl.move(0)
                time.sleep(0.5)
        else: #라인 인식되지 않음
            chassis_ctrl.stop()
            gimbal_ctrl.rotate_with_speed(0,0) #인식을 못했을경우 회전
            time.sleep(0.5) #라인 감지 속도 

def start():
    #turn_Func(200, 2, 90, 1)
    #line_Tracking() 
    test()
    print('line_Tracking end')
    move_Axis(0.7, 0, 0.2, 0.5)
    print('move_Axis end')
    result = number_Detection(1)
    print('result = ', result)
    if result == 1:
        turn_Func(200, 1, 90, 0.5)
    if result == 2:
        turn_Func(200, 2, 90, 0.5)
    print('turn_Func end')
    line_Tracking()
    print('end')
        
    #move_Axis(0.7, 90, 1, 0.5)
    #move_Axis(0.7, 180, 1, 0.5)
    #move_Axis(0.7, -90, 1, 0.5)
    #print(number_Detection(1))