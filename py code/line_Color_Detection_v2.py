def line_Red_Detection():
    cnt = 0
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)
    time.sleep(1)
    while True:
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        cnt += 1
        if list_Num[2] != 0 and cnt >= 10:
            print ('red line')
        if cnt == 15:
            return


def line_Green_Detection():
    cnt = 0
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)
    #media_ctrl.zoom_value_update(4)
    #media_ctrl.exposure_value_update(rm_define.exposure_value_small)
    time.sleep(1)
    while True:
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        cnt += 1
        if list_Num[2] != 0 and cnt >= 10:
            print ('green line')
        if cnt == 15:
            return


def line_Blue_Detection():
    cnt = 0
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    time.sleep(1) 
    while True:
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        cnt += 1
        if list_Num[2] != 0 and cnt >= 10:
            print ('blue line')
        if cnt == 15:
            return



def start():
    line_Red_Detection()
    line_Green_Detection()
    line_Blue_Detection()