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