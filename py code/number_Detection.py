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