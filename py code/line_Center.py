def line_Center(set_time):
    line = RmList()
    V = 0.0
    gimbal_ctrl.pitch_ctrl(-20) 
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow) 
    vision_ctrl.enable_detection(rm_define.vision_detection_line) 
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue) 
    line = RmList(vision_ctrl.get_line_detection_info()) 
    cnt = 0
    start = time.time()
    while not cnt == 1 and (time.time() - start) <= set_time:
        print('time :', time.time() - start)
        if len(line) >= 22:    
            if line[2] != 1:
                cnt = 1
                print('stop because', line[2])
                chassis_ctrl.stop()

            t = line[5]      
            if line[3] >= 0.0:   
                dy = line[3] - 0.5   
            else:
                dy = line[3] + 0.4     
            chassis_ctrl.move_with_speed(V,3 * dy,t * 2) 
        else:
            chassis_ctrl.stop()
        line=RmList(vision_ctrl.get_line_detection_info())