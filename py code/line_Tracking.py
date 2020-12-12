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
