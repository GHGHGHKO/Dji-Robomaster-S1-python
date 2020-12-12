def number_Detection(set_distance):
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(set_distance)
    while True:
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_zero):
            return 0
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
            return 1
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
            return 2
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
            return 3
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four):
            return 4
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_five):
            return 5
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_six):
            return 6
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_seven):
            return 7
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_eight):
            return 8
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_nine):
            return 9

def start():
    while True:
        result = number_Detection(1)
        print('result', result)